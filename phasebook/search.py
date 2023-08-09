from flask import Blueprint, request

from .data.search_data import USERS

bp = Blueprint("search", __name__, url_prefix="/search")

@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200

def search_users(args):
    """Search users database and sort based on priority

    Parameters:
        args: a dictionary containing the search parameters

    Returns:
        a sorted list of users that match the search parameters
    """

    # Extract search parameters from the args dictionary
    search_id = args.get('id')
    search_name = args.get('name')
    search_age = args.get('age')
    search_occupation = args.get('occupation')

    # Initialize a list to store matching users
    matching_users = []

    for user in USERS:
        if search_id is not None and user['id'] == search_id:
            matching_users.append(user)
        elif search_name is not None and search_name.lower() in user['name'].lower():
            matching_users.append(user)
        elif search_age is not None and abs(user['age'] - int(search_age)) <= 1:
            matching_users.append(user)
        elif search_occupation is not None and search_occupation.lower() in user['occupation'].lower():
            matching_users.append(user)
            
    return matching_users

