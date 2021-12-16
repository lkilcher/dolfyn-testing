#import dolfyn as dlfn
import dolfyn0 as dlfn0
#from dolfyn0.test.base import load_tdata
from dolfyn.tests.base import load_ncdata as load1
import numpy as np
import pandas as pd
from datetime import datetime as dt
import numpy as np
import dolfyn as dlfn1
import pdb
load0 = dlfn0.load
import glob
from dolfyn.time import date2epoch
from dolfyn0.data.time import num2date

datadir = 'dolfyn/dolfyn/test/data/'

ALL_FILES = glob.glob(datadir + '*.h5')
ALL_FILES.sort()

def print_all_files():

    for fl in ALL_FILES:
        print(fl.rsplit('/')[-1])

def time2timestamp(time):
    try:
        time = time.values
    except:
        pass
    tmp = np.empty(time.shape, dtype='object')
    for idx, t in enumerate(time):
        tmp[idx] = dt.fromtimestamp(t)
    return pd.to_datetime(tmp)

aliases = [('Error', 'error'),
           ('depth_m', 'depth'),
           ('temperature_C', 'temp'),
           ('echo', 'amp'),
           ('mpt_sec', 'min_preping_wait'),
           ('bt_range', 'dist_bt'),
           ('bt_vel', 'vel_bt'),
           ('bt_ampl', 'amp_bt'),
           ('bt_corr', 'corr_bt'),
           ('bt_perc_gd', 'prcnt_gd_bt'),
           ('bit', 'builtin_test_fail'),
           ('glatitude', 'latitude_gps'),
           ('glongitude', 'longitude_gps'),
           ('ssp', 'c_sound'),
           ('sigma_Uh', 'U_std'),
           ('press', 'pressure'),
           ('velraw', 'vel_raw'),
           ('orient_up', 'orientation'),
           ('ensemble', 'ensemble_count'),
           ('erro', 'error'),
           ('Error', 'error'),
           ]


def check_data(fname, data0, data1):

    if fname == 'AWAC_test01_earth2principal':
        data0 = data0.subset[:500]
        data0.rotate2('earth', inplace=True)
        data0.props['principal_heading'] = round(dlfn0.calc_principal_heading(data0.vel.mean(1),
                                                                        tidal_mode=False), 4)
        data0.rotate2('principal', inplace=True)

    return data0, data1


def compare_file(fname):
    fnm = fname.rsplit('/')[-1].split('.')[0]
    print("")
    print("*********************************")
    print('Checking data for {}...'.format(fname))

    try:
        data0 = load0(fname)
    except FileNotFoundError:
        data0 = load0(datadir + '/' + fname)
    try:
        data1 = load1(fnm + '.nc')
    except FileNotFoundError:
        print("### NO DOLfYN 1.0 FILE ###")
        return data0, None

    data0, data1, match = compare_data(data0, data1)

    if match:
        print("Data matches!")
    else:
        print("### Data Does Not Match ###")
    
    return data0, data1


def compare_data(data0, data1):
    """Compare the DOLfYN 0.12 object `data0` to the DOLfYN 1.0 object `data1`.

    Returns: True if the data match (according to the complex rules defined below), and False otherwise.
    """
    match = True
    for ky in data0.props:
        val0 = data0.props[ky]
        if ky == 'inst2head_rotmat':
            data0['inst2head_rotmat'] = val0
            continue

        if ky == 'Itke_thresh':
            continue

        try:
            if ky=='motion accel_filtfreq Hz' or ky=='motion corrected':
                val1 = data1.attrs[ky]
            else:
                val1 = data1.attrs[ky.replace(' ', '_')]
        except KeyError:
            print("Property '{}' NOT FOUND in new dataset".format(ky))
            continue
        if ky in ['inst_type']:
            if val0 == 'ADP':
                val0 = 'ADCP'

        ### Hard-code some exceptions...
        if ky == 'inst_make' and val0 == 'RDI' and val1 == 'TRDI':
            val0 = val1
        if ky == 'inst_model':
            val0 = val0.lower()
            val1 = val1.lower()
            if val0 == '<workhorse?>' and val1 == 'workhorse':
                val0 = val1
        elif ky == 'rotate_vars':
            _tmp = []
            for val in list(val0):
                if val == 'velraw':
                    val = 'vel_raw'
                if val == 'bt_vel':
                    _tmp.append('vel_bt')
                elif val.startswith('orient.'):
                    if not val.endswith('mag'):
                        _tmp.append(val.split('.')[-1])
                else:
                    _tmp.append(val)
            val1 = [_ky.rsplit('.')[-1] for _ky in val1 if not _ky.startswith('mag')]
            val0 = _tmp
            val0.sort()
            val1.sort()
        elif ky == 'inst2head_vec':
            val0 = list(val0)
        try:
            val1 = val1.tolist()
        except:
            pass
        if val0 == val1:
            continue
        else:
            match = False
            print("Property '{}' does not match".format(ky))

    # Need to put this here because the `data0 = data0.subset[:500]` line was clipping the `range_echo` variable.
    range_echo_flag = False
    if 'range_echo' in data0:
        range_echo_flag = True
        tmp = data0.pop('range_echo')

    if data1.time.shape[0] < data0.mpltime.shape[0]:
        # I've decided this is inconequential. We're just truncating the data on the next line...
        pass
    data0 = data0.subset[:500]
    
    # Shortened VelEchoBT01.ad2cp since it only has 159 profiles
    if data1.inst_type=='ADCP' and hasattr(data1, 'dist_bt'):
        data0 = data0.subset[:100]

    # When we're dealing with very-short datasets (in time), data1 is often longer than data0
    if data0.shape[-1] < data1.time.shape[0]:
        # Just truncate data1 in time
        data1 = data1[{'time':slice(None,data0.shape[-1])}]

    # Put `range_echo` back into the dataset
    if range_echo_flag:
        data0['range_echo'] = tmp

    t0 = np.array(date2epoch(list(num2date(data0.mpltime))))
    if np.allclose(t0, data1.time):
        pass
        #print("    TIME OK!".format(ky))
    else:
        print("!!! TIME DOES NOT MATCH !!!")

    if 'gtime' in data0:
        unique_time, u_inds = np.unique(data0.gtime,
                                        return_index=True)
        for ky in ['glongitude', 'glatitude']:
            data0['orient'][ky] = data0['orient'][ky][u_inds]
        gdi = ~np.isnan(data0.orient.glongitude + data0.orient.glatitude)
        data0.orient.glongitude = data0.orient.glongitude[gdi]
        data0.orient.glatitude = data0.orient.glatitude[gdi]
        
    for ky in data0.iter_data():
        val = data0[ky]
        # Default tolerances for np.allclose below
        rtol = 1e-5
        atol = 1e-8
        nm = ky.rsplit('.')[-1]
        if nm.startswith('mag'):
            # Ignore all the mag variables, always.
            continue
        if nm in ['adc', 'rtc', 'range_echo']:
            # Ignore these variables.
            continue
        if ky.startswith('config'):
            continue
        elif ky in ['props', 'gtime',]:
            continue
        elif 'mpltime' in ky:
            continue
        elif nm in ['glongitude', 'glatitude']:
            if data1['longitude_gps'].shape != data0['orient.glongitude'].shape:
                print("### {} shapes do not match!".format(nm))
                match = False
                continue
        elif ky == 'env.temp' and data0.props['inst_model'] == 'AWAC':
            val /= 100
        elif ky.startswith('range'):
            val = np.around(val, 2)
            if data0.props['inst_model'].startswith('AWAC'):
                val += data0.config['cell_size'] / 2.0
            elif (data0.props['inst_model'].startswith('Sig') or
                  data0.props['inst_model'].startswith('AD2CP')):
                val += data0.config['cell_size']
            #print(val - data1.range)
            atol = 5e-3
        elif ky.endswith('temp_press'):
            atol = 3e-2

        for nm0, nm1 in aliases:
            if nm == nm0 and nm not in data1 and hasattr(data1, nm1):
                nm = nm1
        
        model = data0.props['inst_model']
        if ky.startswith('orient.mag') and (model.startswith('Sig') or model.startswith('AD2CP')):
            val = val/10
        if ky=='echo' and model.startswith('AD2CP'):
            echosounder = data1[nm]*100
            data1[nm] = echosounder.astype("int32")
        elif 'sys.ensemble' in ky:
            tg = ky[12:]
            nm = 'ensemble_count' + tg
            val += 1
        elif 'sys.batt_V' in ky:
            tg = ky.rsplit('.')[-1][6:]
            nm = 'batt' + tg
            data1[nm] = data1[nm].astype("float16")
        elif 'sys.temp_mag' in ky:
            tg = ky.rsplit('.')[-1][8:]
            nm = 'temp_mag' + tg
            data1[nm] = data1[nm].astype("float16")
        elif 'sys.temp_press' in ky:
            tg = ky.rsplit('.')[-1][10:]
            nm = 'temp_press' + tg
            data1[nm] = data1[nm].astype("float16")
        elif ky == 'env.press':
            tg = ky.rsplit('.')[-1][5:]
            nm = 'pressure' + tg
        elif ky == 'Spec.vel':
            nm = 'psd'
        elif 'sys.xmit_energy' in ky:
            tg = ky[15:]
            nm = 'xmit_energy' + tg
            val = np.median(val)
        elif 'sys.ambig_vel' in ky:
            tg = ky[13:]
            nm = 'ambig_vel' + tg
            val = np.median(val.copy())/1000
        elif 'orient_up' in ky:
            nortek_orient = {0:'horizontal', 1:'horizontal', 2:'horizontal',
                            3:'horizontal', 4:'up', 5:'down', 7:'AHRS'}
            val = nortek_orient[np.median(val)]
        elif '_quality' in ky: # ast and alt_quality
            val = val/100
        elif 'ast_dist' in nm or 'alt_dist' in nm:
            data1[nm] = data1[nm].astype("float16")

        if nm == 'vel':
            atol = 1e-6
        if nm in ['orientmat']:
            atol = 1e-3
            rtol = 1e-6
        if nm in ['accel', 'accel_b5', 'mag', 'mag_b5']:
            atol = 1e-5
        if nm in ['batt']:
            atol = 1e-2
        if nm.startswith('temp'):
            rtol = 1e-3
        if nm in ['echo']:
            atol = 1.1
        if nm in ['roll']:
            rtol = 1e-5
            atol = 1e-4
            
        if hasattr(data1, nm):
            if 'roll' in nm:
                #roll is an xarray method
                d = data1[nm]
            else:
                d = getattr(data1, nm)

            if type(d)==str and d==val:
                pass
            elif 'altraw' in ky:
                pass
            elif np.allclose(d, val, rtol=rtol, atol=atol, equal_nan=True):
                    pass # Don't print matches.
                    #print("    {} OK!".format(ky))
            else:
                print("### {} DOES NOT MATCH".format(ky.upper()))
                if ky == 'range':
                    raise Exception
                match = False
        else:
            if 'altraw' in ky:
                pass
            else:
                print('--- {} not in new dataset.'.format(ky))
                match = False
    return data0, data1, match
        
if __name__ == '__main__':

    print_all_files()
