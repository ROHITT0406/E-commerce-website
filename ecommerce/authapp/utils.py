from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six                                           
class TokenGenrator(PasswordResetTokenGenerator):
    def _make_hash_value(self,user,timestamp):
        return (str(user.pk) + str(timestamp) + str(user.is_active))
generate_token=TokenGenrator()