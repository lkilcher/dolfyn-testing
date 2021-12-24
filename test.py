from importlib import reload
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
plt.ion()
import compare_data
reload(compare_data)
from compare_data import compare_file, dlfn0, dlfn1
import numpy as np
from dolfyn.adv import api as avm1
from dolfyn0.adv import api as avm0

if False:
    fnm = 'vector_data_imu01-json_mc'
    # Compare the data that disagrees for this file:
    data0, data1 = compare_file(fnm + '.h5')

    fig1 = fig = plt.figure(100)
    fig.clf()
    fig, axs = plt.subplots(3, 1, num=fig.number, sharex=True)

    for idx in range(3):
        ax = axs[idx]
        ax.plot(data0.vel[idx], color='r')
        ax.plot(data1.vel[idx], color='b')
    axs[0].set_title("VEL")
    fig.savefig('fig/' + fnm + '.VEL.png')

    fig2 = fig = plt.figure(101)
    fig.clf()
    fig, axs = plt.subplots(3, 1, num=fig.number, sharex=True)

    for idx in range(3):
        ax = axs[idx]
        ax.plot(data0.orient.velacc[idx], color='r')
        ax.plot(data1.velacc[idx], color='b')
    axs[0].set_title("VELACC")
    fig.savefig('fig/' + fnm + '.VELACC.png')

    fig3 = fig = plt.figure(102)
    fig.clf()
    fig, axs = plt.subplots(3, 1, num=fig.number, sharex=True)

    for idx in range(3):
        ax = axs[idx]
        ax.plot(data0.orient.acclow[idx], color='r')
        ax.plot(data1.acclow[idx], color='b')
    axs[0].set_title("ACCLOW")
    fig.savefig('fig/' + fnm + '.ACCLOW.png')
    
if False:
    fnm = 'vector_data_imu01_mcDeclin10'
    # Compare the data that disagrees for this file:
    data0, data1 = compare_file(fnm + '.h5')

    fig1 = fig = plt.figure(200)
    fig.clf()
    fig, axs = plt.subplots(3, 1, num=fig.number, sharex=True)

    for idx in range(3):
        ax = axs[idx]
        ax.plot(data0.vel[idx], color='r')
        ax.plot(data1.vel[idx], color='b')
    axs[0].set_title("VEL")
    fig.savefig('fig/' + fnm + '.VEL.png')

    fig2 = fig = plt.figure(201)
    fig.clf()
    fig, axs = plt.subplots(3, 1, num=fig.number, sharex=True)

    for idx in range(3):
        ax = axs[idx]
        ax.plot(data0.orient.velacc[idx], color='r')
        ax.plot(data1.velacc[idx], color='b')
    axs[0].set_title("VELACC")
    fig.savefig('fig/' + fnm + '.VELACC.png')

    fig3 = fig = plt.figure(202)
    fig.clf()
    fig, axs = plt.subplots(3, 1, num=fig.number, sharex=True)

    for idx in range(3):
        ax = axs[idx]
        ax.plot(data0.orient.acclow[idx], color='r')
        ax.plot(data1.acclow[idx], color='b')
    axs[0].set_title("ACCLOW")
    fig.savefig('fig/' + fnm + '.ACCLOW.png')

if False:
    fnm = 'vector_data_imu01_mc'
    # Compare the data that disagrees for this file:
    data0, data1 = compare_file(fnm + '.h5')

    fig1 = fig = plt.figure(300)
    fig.clf()
    fig, axs = plt.subplots(3, 1, num=fig.number, sharex=True)

    for idx in range(3):
        ax = axs[idx]
        ax.plot(data0.vel[idx], color='r')
        ax.plot(data1.vel[idx], color='b')
    axs[0].set_title("VEL")
    fig.savefig('fig/' + fnm + '.VEL.png')

    fig2 = fig = plt.figure(301)
    fig.clf()
    fig, axs = plt.subplots(3, 1, num=fig.number, sharex=True)

    for idx in range(3):
        ax = axs[idx]
        ax.plot(data0.orient.velacc[idx], color='r')
        ax.plot(data1.velacc[idx], color='b')
    axs[0].set_title("VELACC")
    fig.savefig('fig/' + fnm + '.VELACC.png')

    fig3 = fig = plt.figure(302)
    fig.clf()
    fig, axs = plt.subplots(3, 1, num=fig.number, sharex=True)

    for idx in range(3):
        ax = axs[idx]
        ax.plot(data0.orient.acclow[idx], color='r')
        ax.plot(data1.acclow[idx], color='b')
    axs[0].set_title("ACCLOW")
    fig.savefig('fig/' + fnm + '.ACCLOW.png')
    
if False:
    fnm = 'vector_data_imu01_rotate_earth2principal'
    # Compare the data that disagrees for this file:
    data0, data1 = compare_file(fnm + '.h5')

    fig1 = fig = plt.figure(400)
    fig.clf()
    fig, axs = plt.subplots(3, 1, num=fig.number, sharex=True)

    for idx in range(3):
        ax = axs[idx]
        ax.plot(data0.vel[idx], color='r')
        ax.plot(data1.vel[idx], color='b')
    axs[0].set_title("VEL")
    fig.savefig('fig/' + fnm + '.VEL.png')

    fig2 = fig = plt.figure(401)
    fig.clf()
    fig, axs = plt.subplots(3, 1, num=fig.number, sharex=True)

    for idx in range(3):
        ax = axs[idx]
        ax.plot(data0.orient.accel[idx], color='r')
        ax.plot(data1.accel[idx], color='b')
    axs[0].set_title("ACCEL")
    fig.savefig('fig/' + fnm + '.ACCEL.png')

    fig3 = fig = plt.figure(402)
    fig.clf()
    fig, axs = plt.subplots(3, 1, num=fig.number, sharex=True)

    for idx in range(3):
        ax = axs[idx]
        ax.plot(data0.orient.angrt[idx], color='r')
        ax.plot(data1.angrt[idx], color='b')
    axs[0].set_title("ANGRT")
    fig.savefig('fig/' + fnm + '.ANGRT.png')
    
if True:
    fnm = 'vector_data01'
    # Compare the data that disagrees for this file:
    data0, data1 = compare_file(fnm + '.h5')
    # NOTE: THE DATA IN THESE FILES IS IDENTICAL!
    
    bnr1 = avm1.ADVBinner(20, fs=data1.attrs['fs'])
    datb1 = bnr1(data1)

    bnr0 = avm0.TurbBinner(20, fs=data0.props['fs'])
    datb0 = bnr0(data0)

    # Now do the calculations manually...
    u = data0.vel[:,:80].reshape(3,4,20).copy()
    u -= u.mean(-1)[:, :, None]
    tke = (u ** 2).mean(-1)
    stress = np.stack([u[0] * u[1], u[0] * u[2], u[1] * u[2]]).mean(-1)

    fig1 = fig = plt.figure(500)
    fig.clf()
    fig, axs = plt.subplots(3, 1, num=fig.number, sharex=True, sharey=True)

    for idx in range(3):
        ax = axs[idx]
        ax.plot(tke[idx], 'k--', lw=4, label='demean')
        #ax.plot(tke[idx], 'k--', lw=4, label='detrend')
        ax.plot(datb0.tke_vec[idx], color='r', lw=3, label='h5py')
        ax.plot(datb1.tke_vec[idx], color='b', lw=1, label='xarray')
    ax.set_yscale('log')
    ax.legend()
        
    axs[0].set_title("TKE")
    fig.savefig('fig/' + fnm + '.TKE.png')

    fig1 = fig = plt.figure(501)
    fig.clf()
    fig, axs = plt.subplots(3, 1, num=fig.number, sharex=True)
    
    for idx in range(3):
        ax = axs[idx]
        ax.plot(stress[idx], 'k--', lw=4, label='demean')
        ax.plot(datb0.stress[idx], color='r', lw=3, label='h5py')
        ax.plot(datb1.stress[idx], color='b', label='xarray')
    axs[0].set_title("STRESS")
    ax.legend()
    fig.savefig('fig/' + fnm + '.STRESS.png')

    fnm = 'vector_data01_bin'
    data0, data1 = compare_file(fnm + '.h5')
    # Now only n_fft_coh is different, so we'll override this...


if True:
    fnm = 'Sig1000_IMU_rotate_beam2inst'
    # Compare the data that disagrees for this file:
    data0, data1 = compare_file(fnm + '.h5')

    # This data is LITERALLY IDENTICAL (not just 'isclose')!!!
    assert (data0.orient.orientmat == data1.orientmat).all()
    assert (data0.vel == data1.vel).all()
    assert (data0.orient.accel == data1.accel).all()
    assert (data0.orient.angrt == data1.angrt).all()
    assert (data0.orient.accel_b5 == data1.accel_b5).all()
    assert (data0.orient.angrt_b5 == data1.angrt_b5).all()

    edat0 = dlfn0.rotate2(data0, 'earth')
    edat1 = dlfn1.rotate2(data1, 'earth')

    # Load the data from the files that aren't matching:
    fnm = 'Sig1000_IMU_rotate_inst2earth'
    cd0, cd1 = compare_file(fnm + '.h5')

    assert edat0 == cd0

    # Interestingly, this fails:
    # assert (edat1.vel == cd1.vel).all()
    # ...
    # But these all pass:
    assert np.allclose(cd1.vel, edat1.vel)
    assert np.allclose(cd1.angrt, edat1.angrt)
    assert np.allclose(cd1.angrt_b5, edat1.angrt_b5)
    assert np.allclose(cd1.accel, edat1.accel)
    assert np.allclose(cd1.accel_b5, edat1.accel_b5)
    # ... long story short, edat1 == cd1 (approximately)


    fig1 = fig = plt.figure(600)
    fig.clf()
    fig, axs = plt.subplots(4, 1, num=fig.number, sharex=True, sharey=True)

    for idx in range(4):
        ax = axs[idx]
        ax.plot(edat0.vel[idx, 0], color='r', label='h5py')
        ax.plot(edat1.vel[idx, 0], color='b', label='xarray')

    axs[0].set_title("VEL")
    fig.savefig('fig/' + fnm + '.VEL.png')

    fig2 = fig = plt.figure(601)
    fig.clf()
    fig, axs = plt.subplots(3, 1, num=fig.number, sharex=True, sharey=True)

    for idx in range(3):
        ax = axs[idx]
        ax.plot(edat0.orient.accel[idx], color='r', label='h5py')
        ax.plot(edat1.accel[idx], color='b', label='xarray')
        ax.plot(edat0.orient.accel_b5[idx], color='r', ls='--', label='h5py')
        ax.plot(edat1.accel_b5[idx], color='b', ls='--', label='xarray')

    axs[0].set_title("ACCEL")
    fig.savefig('fig/' + fnm + '.ACCEL.png')

    fig3 = fig = plt.figure(602)
    fig.clf()
    fig, axs = plt.subplots(3, 1, num=fig.number, sharex=True, sharey=True)

    for idx in range(3):
        ax = axs[idx]
        ax.plot(edat0.orient.angrt[idx], color='r', label='h5py')
        ax.plot(edat1.angrt[idx], color='b', label='xarray')
        ax.plot(edat0.orient.angrt_b5[idx], color='r', ls='--', label='h5py')
        ax.plot(edat1.angrt_b5[idx], color='b', ls='--', label='xarray')

    axs[0].set_title("ACCEL")
    fig.savefig('fig/' + fnm + '.ANGRT.png')
