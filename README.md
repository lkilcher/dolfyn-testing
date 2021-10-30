# Setup

To get started, first setup and activate a new virtual environment.

Then, if using conda, you can do:

    conda env update -f environment.yml
    pip install -r requirements.txt

Or -- if you're not using conda -- simply do:
    
    pip install -r requirements.txt

# Getting Started

From there, you should be able to run the `run_all.py` script to compare all of the data in the `DOLfYN 0.12` test data directory to the data in the `DOLfYN 0.13` test data (note, `0.13` will soon be `DOLfYN 1.0-beta`):

    python run_all.py

Occassionally we will write the output of this script to a file in this repo by:

    python run_all.py > run_all-output.txt
    
Eventually, we'd like for all of these tests to be totally cleaned up so that every file has an `OK!` next to it. This should happen by one-of-three paths:
    1. By identifying the difference as inconsequential, and filtering it out of the checks in the `compare_data` function
    2. Identify a problem in the dolfyn-0.12 data -- and probably just fixing it in the `compare_data` function inside of `compare_data.py`
    3. By fixing the dolfyn-1.0 code and test data

Let's plan to discuss all of the inconsistencies that are captured in `run_all_output.txt` on [this pull request](https://github.com/lkilcher/dolfyn-testing/pull/2/files).

# Detailed inspection of individual files

It's also possible to inspect the difference between individual files interactively using:

    >>> from compare_data import compare_file
    >>> data0, data1 = compare_file('winriver01.h5')

    *********************************
    Checking data for winriver01.h5...
    Property 'inst_make' does not match
    Property 'inst_model' does not match
    Property 'rotate_vars' does not match
    --- bt_range not in new dataset. ---
    --- bt_vel not in new dataset. ---
    --- depth_m not in new dataset. ---
        env.salinity OK!
    --- env.temperature_C not in new dataset. ---
    --- gtime not in new dataset. ---
    --- mpltime not in new dataset. ---
    --- orient.glatitude not in new dataset. ---
    --- orient.glongitude not in new dataset. ---
        orient.orientmat OK!
        range OK!
    --- signal.bt_ampl not in new dataset. ---
    --- signal.bt_corr not in new dataset. ---
    --- signal.bt_perc_gd not in new dataset. ---
        signal.corr OK!
    --- signal.echo not in new dataset. ---
        signal.prcnt_gd OK!
    --- sys.adc not in new dataset. ---
    --- sys.bit not in new dataset. ---
    --- sys.mpt_sec not in new dataset. ---
    --- sys.number not in new dataset. ---
    --- sys.rtc not in new dataset. ---
    --- sys.ssp not in new dataset. ---
    ### VEL DOES NOT MATCH ###
    ### Data Does Not Match ###

You can then inspect the differences summarized in the stdout of that function by looking at the data objects returned by it. For example, you might do:

    >>> data0.vel - data1.vel

It's also possible to show a list of all the test files by either calling `compare_data.py` as a script from the command line, or by calling the function `print_all_files()` interactively:

    >>> from compare_data import print_all_files
    >>> print_all_files()
    
    AWAC_test01.h5
    AWAC_test01_earth2inst.h5
    AWAC_test01_earth2principal.h5
    AWAC_test01_inst2beam.h5
    AWAC_test01_ud.h5
    BenchFile01.h5
    BenchFile01_rotate_beam2inst.h5
    BenchFile01_rotate_earth2principal.h5
    BenchFile01_rotate_inst2earth.h5
    RDI_test01.h5
    RDI_test01_rotate_beam2inst.h5
    RDI_test01_rotate_earth2principal.h5
    RDI_test01_rotate_inst2earth.h5
    RDI_withBT.h5
    Sig1000_IMU.h5
    Sig1000_IMU_rotate_beam2inst.h5
    Sig1000_IMU_rotate_inst2earth.h5
    Sig1000_IMU_ud.h5
    VelEchoBT01.h5
    VelEchoBT01_rotate_beam2inst.h5
    burst_mode01.h5
    vector_data01.h5
    vector_data01_bin.h5
    vector_data01_rotate_earth2principal.h5
    vector_data01_rotate_inst2beam.h5
    vector_data01_rotate_inst2earth.h5
    vector_data01_subset.h5
    vector_data01_uclean.h5
    vector_data_imu01-json.h5
    vector_data_imu01-json_mc.h5
    vector_data_imu01.h5
    vector_data_imu01_head_pitch_roll.h5
    vector_data_imu01_mc.h5
    vector_data_imu01_mcDeclin10.h5
    vector_data_imu01_rotate_earth2principal.h5
    vector_data_imu01_rotate_inst2beam.h5
    vector_data_imu01_rotate_inst2earth.h5
    winriver01.h5
    winriver02.h5
    winriver02_rotate_ship2earth.h5


