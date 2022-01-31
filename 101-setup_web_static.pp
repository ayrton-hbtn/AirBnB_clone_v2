# ieiiii puppetts
# plaza sesamoooo

exec {'0':command => '/usr/bin/env apt update',}
-> exec {'1':command => '/usr/bin/env apt install nginx -y',}
-> exec {'2':command => '/usr/bin/env mkdir -p /data/web_static/shared/',}
-> exec {'3':command => '/usr/bin/env mkdir -p /data/web_static/releases/test/',}
-> exec {'4':command => '/usr/bin/env echo "</html>" > /data/web_static/releases/test/index.html',}
-> exec {'5':command => '/usr/bin/env ln -sf /data/web_static/releases/test/ /data/web_static/current',}
-> exec {'6':command => '/usr/bin/env chown -R ubuntu /data',}
-> exec {'7':command => '/usr/bin/env chgrp -R ubuntu /data',}
-> exec {'8':command => '/usr/bin/env sed -i "/listen 80 default_server/a location /hbnb_static/ { alias /data/web_static/current/; }" /etc/nginx/sites-available/default',}
-> exec {'9':command => '/usr/bin/env service nginx restart',}
