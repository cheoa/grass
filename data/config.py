MIN_PROXY_SCORE = 50

CLAIM_REWARDS_ONLY = False  # claim tiers rewards only (https://app.getgrass.io/dashboard/referral-program)

THREADS = 1 # for register account / claim rewards mode only

CHECK_POINTS = True  # show point for each account every nearly 10 minutes

STOP_ACCOUNTS_WHEN_SITE_IS_DOWN = True  # stop account for 20 minutes, to reduce proxy traffic usage

SHOW_LOGS_RARELY = True  # not always show info about actions to decrease pc influence

APPROVE_EMAIL_ONLY = False  # approve email (without imap and access to email)

# REGISTER PARAMETRS ONLY
REGISTER_ACCOUNT_ONLY = False
REGISTER_DELAY = (3, 7)

TWO_CAPTCHA_API_KEY = ""
ANTICAPTCHA_API_KEY = ""
CAPMONSTER_API_KEY = ""
CAPSOLVER_API_KEY = "CAP-10468D1DB03F6D696CBC2D481F6FF497"
CAPTCHAAI_API_KEY = ""

# Captcha params, left empty
CAPTCHA_PARAMS = {
    "captcha_type": "v2",
    "invisible_captcha": False,
    "sitekey": "6LeeT-0pAAAAAFJ5JnCpNcbYCBcAerNHlkK4nm6y",
    "captcha_url": "https://app.getgrass.io/register"
}

########################################

ACCOUNTS_FILE_PATH = "data/accounts.txt"
PROXIES_FILE_PATH = "data/proxies.txt"
