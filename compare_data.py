#import dolfyn as dlfn
import dolfyn0 as dlfn0
#from dolfyn0.test.base import load_tdata
from dolfyn.tests.base import load_ncdata as load1
import numpy as np
import glob
import pandas as pd
from datetime import datetime as dt
import numpy as np
import dolfyn as dlfn1
import pdb


###### IMPORTANT!!!!
# Need to replace the pkl.py file in pyDictH5 with the one here in order for this to work!

from io import StringIO 
import sys


def time2timestamp(time):
    try:
        time = time.values
    except:
        pass
    tmp = np.empty(time.shape, dtype='object')
    for idx, t in enumerate(time):
        tmp[idx] = dt.fromtimestamp(t)
    return pd.to_datetime(tmp)


class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio    # free up some memory
        sys.stdout = self._stdout


def compare_data(data0, data1):
    match = True
    for ky in data0.props:
        val0 = data0.props[ky]
        try:
            val1 = data1.attrs[ky.replace(' ', '_')]
        except KeyError:
            print("Property '{}' NOT FOUND in new dataset".format(ky))
            continue
        if ky in ['inst_type']:
            if val0 == 'ADP':
                val0 = 'ADCP'
        elif ky in ['rotate_vars', 'inst2head_vec']:
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

    if data1.time.shape[0] < data0.mpltime.shape[0]:
        print("Data-new is shorter than data old!")

    # Need to put this here because the `data0 = data0.subset[:500]` line was clipping the `range_echo` variable.
    range_echo_flag = False
    if 'range_echo' in data0:
        range_echo_flag = True
        tmp = data0.pop('range_echo')

    data0 = data0.subset[:500]

    # When we're dealing with very-short datasets (in time), data1 is often longer than data0
    if data0.shape[-1] < data1.time.shape[0]:
        # Just truncate data1 in time
        data1 = data1[{'time':slice(None,data0.shape[-1])}]

    # Put `range_echo` back into the dataset
    if range_echo_flag:
        data0['range_echo'] = tmp
    
    for ky in data0.iter_data():
        val = data0[ky]

        # Default tolerances for np.allclose below
        rtol = 1e-5
        atol = 1e-8
        
        if ky.startswith('config'):
            continue
        elif ky in ['props']:
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
        nm = ky.rsplit('.')[-1]
        if ky == 'Spec.vel':
            nm = 'spec'
        if nm in data1:
            if np.allclose(data1[nm], val, rtol=rtol, atol=atol):
                print("    {} OK!".format(ky))
            else:
                print("### {} DOES NOT MATCH ###".format(ky.upper()))
                if ky == 'range':
                    error
                match = False
        else:
            print('--- {} not in new dataset. ---'.format(ky))
    return match
        
if __name__ == '__main__':
    datadir = 'dolfyn/dolfyn/test/data/'
    files = glob.glob(datadir + '*.h5')
    files.sort()

    import time
    
    for ffname in files:
        fnm = ffname.rsplit('/')[-1].split('.')[0]
        print("")
        print("*********************************")
        print('Checking data for {}...'.format(fnm), end='')

        data0 = dlfn0.load(ffname)
        try:
            data1 = load1(fnm + '.nc')
        except FileNotFoundError:
            print("### NO DOLfYN 1.0 FILE ###")
            continue

        with Capturing() as output:
            match = compare_data(data0, data1)

        if match:
            print(" OK!")
        else:
            print()
            for line in output:
                print(line)
