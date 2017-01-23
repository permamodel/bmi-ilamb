from nose.tools import raises
from bmi_ilamb.cmd.run import main


_HERE = path.abspath(path.dirname(__file__))


def setup_module():
    """Fixture called before any tests are performed."""
    print('\n*** ' + __name__)
        

@raises(SystemExit)
def test_run_fails_with_no_parameters():
    main()
