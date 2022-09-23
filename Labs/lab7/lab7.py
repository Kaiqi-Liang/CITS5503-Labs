from fabric import Connection
conn = Connection('ec2')

res = conn.sudo('apt-get update')
res = conn.sudo('apt-get upgrade')
res = conn.sudo('apt install python3-pip')
res = conn.sudo('apt install nginx')
res = conn.put('default', 'default')
res = conn.sudo('mv default /etc/nginx/sites-enabled/default')
res = conn.sudo('service nginx restart')

res = conn.sudo('apt install python3-pip')
res = conn.sudo('pip install django')
res = conn.sudo('mkdir -p /opt/wwc/mysites')
res = conn.put('lab.tar', 'lab.tar')
res = conn.sudo('tar xf lab.tar -C /opt/wwc/mysites/')
res = conn.run('cd /opt/wwc/mysites/lab; sudo python3 manage.py runserver 8000')
