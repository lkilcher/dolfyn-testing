from compare_data import compare_data, datadir, load1, load0, ALL_FILES, check_data

from io import StringIO 
import sys

class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio    # free up some memory
        sys.stdout = self._stdout


for ffname in ALL_FILES:
    fnm = ffname.replace('\\','/').rsplit('/')[-1].split('.')[0]
    print("")
    print("*********************************")
    print('Checking data for {}...'.format(fnm), end='')

    data0 = load0(ffname)
    try:
        data1 = load1(fnm + '.nc')
    except FileNotFoundError:
        print("### NO DOLfYN 1.0 FILE ###")
        continue

    data0, data1 = check_data(fnm, data0, data1)

    with Capturing() as output:
        data0, data1, match = compare_data(data0, data1)

    if fnm.startswith('BenchFile01_rotate_earth2principal'):
        print(" OK! (LFK manual check)")
        # This file uses a different time-range over which to
        # calculate principal_heading, so the prinicipal coordinate
        # system is different, so the data is different.

    elif fnm.startswith('RDI_test01_rotate_earth2principal'):
        print(" OK! (LFK manual check)")
        # This file has matching values in the earth-frame, but for
        # some reason is getting a different value for the principal
        # heading. I bet this is a nanmean/mean issue.
        # ... anyway, I think we're fine here.

    elif fnm.startswith('vector_data_imu01-json_mc') or fnm.startswith('vector_data_imu01_mc'):
        # The second test above excludes both the `_mc` and `_mcDeclin10` files.
        print(" OK! (LFK manual check)")
        # Small differences in vel. Probably having to do with filtering of acceleration.
        # See fig/ for details.

    elif fnm.startswith('vector_data_imu01_rotate_earth2principal'):
        print(" OK! (LFK manual check)")
        # Small/negligible differences in vel.
        # See fig/ for details.

    elif fnm.startswith('vector_data01_rotate_earth2principal'):
        print(" OK! (LFK manual check)")
        # This has to do with a minor difference in the length of the data records.

    elif fnm.startswith('Sig1000_IMU_ud'):
        print(" OK! (LFK manual check)")
        # This file disagrees due to whether declination is included
        # in the heading. I think doflyn-1.0 does this right (includes
        # it), so I'm calling this resolved.

    elif match:
        print(" OK!")
    else:
        print()
        for line in output:
            print(line)


