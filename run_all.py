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

    if match:
        print(" OK!")
    else:
        print()
        for line in output:
            print(line)


