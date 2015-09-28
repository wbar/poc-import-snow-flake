from django.db import models


class SaleFacts(models.Model):
    """
    Model for Sale fact
    """
    transaction_uid = models.UUIDField(
        unique=True,
        verbose_name='Transaction unique identifier',
        help_text='A reference number which is generated automatically recording each published sale. '
                  'The number is unique and will change each time a sale is recorded.',
        db_index=True
    )
    date_of_transfer = models.ForeignKey(
        'DateDictionary',
        help_text='Date when the sale was completed, as stated on the transfer deed.'
    )
    price = models.PositiveIntegerField(
        help_text='Sale price stated on the transfer deed.'
    )

    area_code = models.ForeignKey('AreaCodesDictionary')
    property_type = models.ForeignKey('PropertyTypesDictionary')
    new_property = models.ForeignKey('NewPropertyTypesDictionary')
    duration = models.ForeignKey('DurationTypesDictionary')

    class Meta:
        verbose_name = 'Sale fact'
        verbose_name_plural = 'Sale facts'
        abstract = True
