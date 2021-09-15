from . import accounts, classes, courses, homeworks, posts, quizzes

routers = (
    { "router": accounts.authrouter, "prefix": "/auth", "tags": ["Sign in"] },
    { "router": accounts.authresetpasswordrouter, "prefix": "/auth", "tags": ["Reset password"] },
    { "router": accounts.registerrouter, "prefix": "/auth", "tags": ["Register"] },

    { "router": accounts.usersrouter, "prefix": "/accounts", "tags": ["Accounts"] },

    { "router": classes.section_router },
    { "router": classes.classe_router },
    { "router": classes.level_router },

    { "router": courses.course_router },
    { "router": courses.course_section_router },

    { "router": homeworks. homework_router},
    { "router": homeworks.homework_completed_router },

    { "router": posts.comment_router},
    { "router": posts.post_router },
    { "router": posts.page_router},

    { "router": quizzes.quiz_router},
    { "router": quizzes.quiz_completed_router },
    { "router": quizzes.question_router},
    { "router": quizzes.answer_router},
    { "router": quizzes.question_answer_router },
)
