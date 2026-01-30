

Things to do:

1. give permission flow: the user needs to be redirected to strava and then strava sends back a "exchange token", this exchange token, then needs to be exchanged for the actual auth bearer token and the refresh token.
2. refresh when auth token has expired: the auth token expires often and the refresh token is needed to get a new auth token
3. once done we cna use the api to get activities

next: webhooks

1. need to make a manual post request to subscribe to the webhook
2. webhooks are sent when
    - access to the app is revoked in strava
    - activity is created
    - activity is deleted
    - activity fields are updated: title, type, privacy


https://developers.strava.com/docs/webhooks/