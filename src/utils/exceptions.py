from fastapi import HTTPException, status


def raise_not_found_exception(reason: str = "entity does not exist"):
    """ Raise not found exeption """
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail={
            "code": 404,
            "reason": reason,
        },
    )


def raise_unprocessable_entity_exception(reason: str = "unable to process the contained instructions"):
    """ Raise not found exeption """
    raise HTTPException(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        detail={
            "code": 422,
            "reason": reason,
        },
    )
