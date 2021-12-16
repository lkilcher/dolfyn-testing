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
    
if True:
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
    
