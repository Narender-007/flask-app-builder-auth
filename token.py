from adal import AuthenticationContext

authority_url = "https://login.microsoftonline.com/693ed5a4-aca9-44c1-a9be-ae17e6b50e7e"
client_id = "ac86ce12-33bf-4708-8f1c-248184c935e2"
client_secret = "ebS8Q~gg3EGsYsBzY6GyTR.h5AsaymtDDr6Via15"
resource = "https://graph.microsoft.com"  # e.g., https://graph.microsoft.com

context = AuthenticationContext(authority_url)
token_response = context.acquire_token_with_client_credentials(resource, client_id, client_secret)

access_token = token_response['accessToken']
print("Access token:", access_token)











# # Example Flask configuration for Azure AD OIDC
# from flask import Flask
# from authlib.integrations.flask_client import OAuth

# app = Flask(__name__)

# app.config['SECRET_KEY'] = '12345678901234567890'
# app.config['OAUTH_CLIENT_ID'] = 'ac86ce12-33bf-4708-8f1c-248184c935e2'
# app.config['OAUTH_CLIENT_SECRET'] = 'ebS8Q~gg3EGsYsBzY6GyTR.h5AsaymtDDr6Via15'
# app.config['OAUTH_DISCOVERY_URL'] = 'https://login.microsoftonline.com/your_tenant_id/v2.0/.well-known/openid-configuration'
# # The above URL is the "OpenID Connect metadata document" URL from Azure AD
# # It will contain the "jwks_uri" that the OIDC library will use for token validation

# oauth = OAuth(app)
# oauth.register(name='azure', server_metadata_url=app.config['OAUTH_DISCOVERY_URL'])
# @app.route("/")
# def hello():
#     return "Hello, World!"
