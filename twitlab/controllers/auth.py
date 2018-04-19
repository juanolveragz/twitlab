from sqlalchemy.orm import sessionmaker

from twitlab.models.auth import User, Group
from twitlab import engine


def create_or_update_user(user):
    """ Creates or updates a new user.

        This method validate and create a new user object. If the user already
        exists its data will be updated.

        Args:
        - user twitlab.models.User The user to be stored 
    """
    s = _cs(engine)
    s.add(user)
    s.commit()


def _cs(e):
    """ Creates a new session with the given engine.

        Args:
        - e an sqlalchemy Engine

        returns a sqlalchemy session.
    """
    Session = sessionmaker(e)
    return Session()