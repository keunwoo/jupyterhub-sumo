local_config = {
    'oauth_callback_url': '__OAUTH_CALLBACK_URL__',
    'oauth_client_id': '__OAUTH_CLIENT_ID__',
    'oauth_client_secret': '__OAUTH_CLIENT_SECRET__',
    'whitelist': ['__BOOTSTRAP_USER__'],
    'admin_users': ['__BOOTSTRAP_USER__'],
}

# Use GitHub with local account creation.
c.JupyterHub.authenticator_class = 'oauthenticator.LocalGitHubOAuthenticator'
c.GitHubOAuthenticator.oauth_callback_url = local_config['oauth_callback_url']
c.GitHubOAuthenticator.client_id = local_config['oauth_client_id']
c.GitHubOAuthenticator.client_secret = local_config['oauth_client_secret']
c.Authenticator.whitelist = set(local_config['whitelist'])
c.Authenticator.admin_users = set(local_config['admin_users'])

# Use sudospawner; reduces attack surface marginally.
c.JupyterHub.spawner_class = 'sudospawner.SudoSpawner'
c.SudoSpawner.debug_mediator = True

# Allow LocalAuthenticator to create system users, using the config
# implied by the mkuser script below.
c.LocalAuthenticator.create_system_users = True
c.LocalAuthenticator.group_whitelist = ['jupyterusers']
c.LocalAuthenticator.add_user_cmd = ['sudo', '/vagrant/bin/adduser-jupyter.sh']
