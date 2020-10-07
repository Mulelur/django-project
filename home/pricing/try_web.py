from django.utils.safestring import mark_safe

class TryWebEigth():
    line_1 = '1'
    line_2 = '2'
    line_3 = '3'
    line_4 = '4'
    line_5 = '5'

    def get_try_price(self):
        return mark_safe('<p class="pricing-value"><span class="price font-xl">{}</span></p>'.format(0))
