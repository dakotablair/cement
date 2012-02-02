"""Tests for cement.core.exc."""

from nose.tools import with_setup, ok_, eq_, raises
from nose import SkipTest

from cement2.core import exc
from cement2 import test_helper as _t
_t.prep()

def startup():
    pass

def teardown():
    pass

@raises(exc.CementConfigError)    
@with_setup(startup, teardown)
def test_cement_config_error():
    try:
        raise exc.CementConfigError("CementConfigError Test")
    except exc.CementConfigError as e:
        eq_(e.msg, "CementConfigError Test")
        eq_(e.__str__(), "CementConfigError Test")
        raise
        
@raises(exc.CementRuntimeError)
@with_setup(startup, teardown)
def test_cement_runtime_error():
    try:
        raise exc.CementRuntimeError("CementRuntimeError Test")
    except exc.CementRuntimeError as e:
        eq_(e.msg, "CementRuntimeError Test")
        eq_(e.__str__(), "CementRuntimeError Test")
        raise
        
@raises(exc.CementArgumentError)
@with_setup(startup, teardown)
def test_cement_argument_error():
    try:
        raise exc.CementArgumentError("CementArgumentError Test")
    except exc.CementArgumentError as e:
        eq_(e.msg, "CementArgumentError Test")
        eq_(e.__str__(), "CementArgumentError Test")
        raise

@raises(exc.CementInterfaceError)
@with_setup(startup, teardown)
def test_cement_interface_error():
    try:
        raise exc.CementInterfaceError("CementInterfaceError Test")
    except exc.CementInterfaceError as e:
        eq_(e.msg, "CementInterfaceError Test")
        eq_(e.__str__(), "CementInterfaceError Test")
        raise

@raises(exc.CementSignalError)
@with_setup(startup, teardown)
def test_cement_signal_error():
    try:
        import signal
        raise exc.CementSignalError(signal.SIGTERM, 5)
    except exc.CementSignalError as e:
        eq_(e.signum, signal.SIGTERM)
        eq_(e.frame, 5)
        raise