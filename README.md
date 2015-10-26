component-zabbix
===============

Version 1.0-43p
---------------

<img src="https://s3.amazonaws.com/qubell-images/zabbix-logo.png">

Installs and configures Zabbix Server Monitoring

[![Install](https://raw.github.com/qubell-bazaar/component-skeleton/master/img/install.png)](https://express.qubell.com/applications/upload?metadataUrl=https://raw.github.com/qubell-bazaar/component-zabbix/1.0-43p/meta.yml)

Features
--------

- Install and configure Zabbix Server
- Install and configure Zabbix Agent on linux/windows OS example

Configurations
--------------
- Zabbix Server 2.2 CentOS 6.5 (us-east-1/ami-8997afe0), AWS EC2 m1.small, root
- Zabbix Agent App 2.2 CentOS 6.5 (us-east-1/ami-8997afe0), AWS EC2 m1.small, root
- Zabbix Agent App 2.2  Windows 2008 R2 (us-east-1/ami-31620c54), AWS EC2 m3.large, Administrator

Pre-requisites
--------------
 - Configured Cloud Account a in chosen environment
 - Either installed Chef on target compute OR launch under root
 - Internet access from target compute:
   - Zabbix distribution
   - S3 bucket with Chef recipes: qubell-starter-kit-artifacts
   - If Chef is not installed: please install Chef 10.16.2 using http://www.opscode.com/chef/install.sh ```bash <($WGET -O - http://www.opscode.com/chef/install.sh) -v $CHEF_VERSION```

Implementation notes
--------------------
 - Installation is based on Chef recipes from https://github.com/qubell-bazaar/cookbook_qubell_zabbix

Configuration parameters
------------------------
Zabbix Server
- input.recipe-url: URL to Zabbix chef recipe repo
- input.web-credentials: Zabbix server administrator user credentials
- input.image: AWS ami to use

Zabbix Agent
- input.image: AWS ami to use
- input.windows-password: Set Windows administrator user password

Commands parameters
-------------
Run API command
This command will run any API command.
- connection: Connection credentials (object {zabbix-api-ur, user, password})
- method: Zabbix API method to use (string)
- api-params: Zabbix API data (object)

Initialize agent host

This command will install Zabbix Agent an host and initialize it in Zabbix Server
- agent-hosts: List of hosts to initialize. Provide Host IP or FQDN
- identity: Root user on host
- agent-screens: Command will return Host screen ID

Delete hosts from monitoring

This command will delete host from monitoring system
- agent-hosts: List of hosts to delete. Provide Host IP or FQDN
