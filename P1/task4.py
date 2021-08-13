"""
Active Directory
In Windows Active Directory, a group can consist of user(s) and group(s) themselves. We can construct this hierarchy as such. Where User is represented by str representing their ids.
"""


class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")
sub_child2 = Group("subchild2")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
child.add_group(sub_child2)
parent.add_group(child)

"""
Write a function that provides an efficient look up of whether the user is in a group.
"""


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    result = False
    users = group.get_users()
    if user in users:
        return True

    groups = group.get_groups()
    for group in groups:
        users = group.get_users()
        if user in users:
            return True
        else:
            if group.get_groups():
                result = is_user_in_group(user, group)

    return result


print(is_user_in_group(sub_child_user, parent))  # True

sub_child_user1 = "sub_child_user1"
sub_child.add_user(sub_child_user1)
print(is_user_in_group(sub_child_user, parent))  # True

sub_child_user2 = "sub_child_user2"
print(is_user_in_group(sub_child_user2, parent))  # False

sub_child_user3 = "sub_child_user3"
print(is_user_in_group(sub_child_user3, parent))  # False

sub_child_user4 = "sub_child_user4"
print(is_user_in_group(sub_child_user4, sub_child2))  # False
