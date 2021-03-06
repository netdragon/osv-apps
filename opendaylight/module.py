from osv.modules import api

default = api.run_java(
    jvm_args=[
        '-Xms128M',
        '-Xmx2048m',
        '-XX:+UnlockDiagnosticVMOptions',
        '-XX:+UnsyncloadClass',
        '-XX:MaxPermSize=512m',
        '-Dcom.sun.management.jmxremote',
        '-Djava.endorsed.dirs=/opendaylight/lib/endorsed',
        '-Djava.ext.dirs=/usr/lib/jvm/java/jre/lib/ext:/usr/java/packages/lib/ext:/opendaylight/lib/ext',
        '-Dkaraf.instances=/opendaylight/instances',
        '-Dkaraf.home=/opendaylight',
        '-Dkaraf.base=/opendaylight',
        '-Dkaraf.data=/opendaylight/data',
        '-Dkaraf.etc=/opendaylight/etc',
        '-Djava.io.tmpdir=/opendaylight/data/tmp',
        '-Djava.util.logging.config.file=/opendaylight/etc/java.util.logging.properties',
        '-Dkaraf.startLocalConsole=true',
        '-Dkaraf.startRemoteShell=true',
    ],
    classpath=[
        '/opendaylight/lib/karaf.branding-1.1.0-Lithium.jar',
        '/opendaylight/lib/karaf-jaas-boot.jar',
        '/opendaylight/lib/karaf.jar',
        '/opendaylight/lib/karaf-jmx-boot.jar',
        '/opendaylight/lib/karaf-org.osgi.core.jar',
    ],
    args=[
        'org.apache.karaf.main.Main'
    ]
)
