from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class Profile(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    date_of_birth = models.DateField()
    account_balance = models.DecimalField(max_digits=8, decimal_places=2)

    def reset_profile(self):
        # TODO: Implement
        pass

    def modify_balance(self, amount):
        # Modify account balance by <amount> (negative amount to deduct balance)
        # TODO: Implement
        pass


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField(('email address'), unique=True)
    account_lock = models.BooleanField(default=False)
    verified = models.BooleanField(default=False)
    profile = models.OneToOneField(
        Profile,
        on_delete=models.CASCADE,
        null=True
    )
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def add_favourite(self):
        # TODO: Implement
        pass


class AccessTokenManager(models.Manager):
    def generate_token(self, user_id, type, lifespan):
        # TODO: Implement
        pass

    def verify_token(self, token):
        # TODO: Implement
        pass


class AccessToken(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=25)
    token = models.CharField(max_length=36)
    date_created = models.DateTimeField(auto_now_add=True)
    lifespan = models.IntegerField()
    expired = models.BooleanField(default=False)
    objects = AccessTokenManager()


class Authentication():
    @staticmethod
    def register(email, password):
        # TODO: Implement
        pass

    @staticmethod
    def login(email, password):
        # TODO: Implement
        pass

    @staticmethod
    def softlock_user(user_id):
        # TODO: Implement
        pass

    @staticmethod
    def reset_password(user_id):
        # Generate access token and send email with reset link
        # TODO: Implement
        pass

    @staticmethod
    def verify_user(user_id):
        # Generate access token and send email with verification link
        # TODO: Implement
        pass


class StockManager(models.Manager):
    def search_stock(self, search_term):
        # TODO: Implement
        pass


class Stock(models.Model):
    stock_symbol = models.CharField(max_length=15)
    company_name = models.CharField(max_length=45)
    company_desc = models.TextField()
    sector = models.CharField(max_length=45)
    industry = models.CharField(max_length=45)
    image_url = models.URLField()
    objects = StockManager()


class StockPriceCurManager(models.Manager):
    def update_prices(self):
        # TODO: Implement
        pass


class StockPriceCurrent(models.Model):
    stock = models.OneToOneField(
        Stock,
        on_delete=models.CASCADE
    )
    open = models.DecimalField(max_digits=8, decimal_places=2)
    close = models.DecimalField(max_digits=8, decimal_places=2)
    high = models.DecimalField(max_digits=8, decimal_places=2)
    low = models.DecimalField(max_digits=8, decimal_places=2)
    objects = StockPriceCurManager()


class StockPriceHistManager(models.Manager):
    def append_daily_prices(self):
        # TODO: Implement
        pass


class StockPriceHistory(StockPriceCurrent):
    date = models.DateField(auto_now_add=True)
    market_cap = models.DecimalField(max_digits=8, decimal_places=2)
    volume = models.IntegerField()
    objects = StockPriceHistManager()


class Favourites(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)


class TransactionManager(models.Manager):
    def purchase_option(self, user_id, stock_id, option):
        # TODO: Implement
        pass

    def sell_option(self, user_id, transaction_id):
        # TODO: Implement
        pass


class Transaction(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default="Anonymous")
    stock = models.ForeignKey(Stock, on_delete=models.SET_DEFAULT, default="Removed")
    transaction_date = models.DateTimeField(auto_now_add=True)
    purchase_price = models.DecimalField(max_digits=8, decimal_places=2)
    return_price = models.DecimalField(max_digits=8, decimal_places=2)
    lot_quantity = models.IntegerField()
    option = models.CharField(max_length=10)
    active = models.BooleanField(default=True)
    objects = TransactionManager()
