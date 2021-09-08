from . import accounts, classes

routers = (
    { "router": accounts.authrouter, "prefix": "/auth", "tags": ["Sign in"] },
    { "router": accounts.authresetpasswordrouter, "prefix": "/auth", "tags": ["Reset password"] },
    { "router": accounts.registerrouter, "prefix": "/auth", "tags": ["Register"] },

    { "router": accounts.usersrouter, "prefix": "/accounts", "tags": ["Accounts"] },

    { "router": classes.section_router },
    { "router": classes.classe_router },
    { "router": classes.level_router },
)
