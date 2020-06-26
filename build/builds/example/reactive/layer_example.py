from charms.reactive import when, when_not, set_state, set_flag
from charmhelpsers.core.hookenv import application_version_set, status_set
from charmhelpers.fetch import get_upstream_version
import subprocess as sp

@when_not('example.installed')
def install_example():
    set_flag('example.installed')

@when('apt.installed.hello')
def set_message_hello():
    # set the upstream version of hello for juju status
    application_version_set(get_upstream_version('hello'))

    # run hello and get the message
    message = sp.check_output('hello', stderr=sp.STDOUT)

    # set the active status with the message
    status_set('active', message)

    #signal that we know the version of hello
    set_flag('hello.version.set')


    # Do your setup here.
    #
    # If your charm has other dependencies before it can install,
    # add those as @when() clauses above., or as additional @when()
    # decorated handlers below
    #
    # See the following for information about reactive charms:
    #
    #  * https://jujucharms.com/docs/devel/developer-getting-started
    #  * https://github.com/juju-solutions/layer-basic#overview
    #
    # set_flag('layer-example.installed')
