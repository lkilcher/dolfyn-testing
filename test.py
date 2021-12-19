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
    U = data0.vel[:,:80].reshape(3,4,20).copy()
    u -= u.mean(-1)[:, :, None]
    tke = (u ** 2).mean(-1)
    stress = np.stack([u[0] * u[1], u[0] * u[2], u[1] * u[2]]).mean(-1)

    fig1 = fig = plt.figure(500)
    fig.clf()
    fig, axs = plt.subplots(3, 1, num=fig.number, sharex=True, sharey=True)

    for idx in range(3):
        ax = axs[idx]
        ax.plot(tke[idx], 'k--', lw=4, label='TRUTH')
        ax.plot(datb0.tke_vec[idx], color='r', label='h5py')
        ax.plot(datb1.tke_vec[idx], color='b', label='xarray')
    ax.set_yscale('log')
    ax.legend()
        
    axs[0].set_title("TKE")
    fig.savefig('fig/' + fnm + '.TKE.png')

    fig1 = fig = plt.figure(501)
    fig.clf()
    fig, axs = plt.subplots(3, 1, num=fig.number, sharex=True)
    
    for idx in range(3):
        ax = axs[idx]
        ax.plot(stress[idx], 'k--', lw=4, label='TRUTH')
        ax.plot(datb0.stress[idx], color='r', label='h5py')
        ax.plot(datb1.stress[idx], color='b', label='xarray')
    axs[0].set_title("STRESS")
    ax.legend()
    fig.savefig('fig/' + fnm + '.STRESS.png')
