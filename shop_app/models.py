from django.db import models

class User(models.Model):
    first_name = models.CharField("Имя пользователя")
    last_name = models.CharField("Фамилия")
    email = models.EmailField("Почта")
    phone = models.CharField("Номер")

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["first_name", "last_name"]
        indexes = [
            models.Index(fields=["first_name"])
        ]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Order(models.Model):
    ST = [
        ("Оформлен", "Оформлен"),
        ("Отправлен", "Отправлен"),
        ("Доставлен", "Доставлен")
    ]

    PM = [
        ("Банковская карта", "Банковская карта"),
        ("При получении", "При получении")
    ]


    id_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    status = models.CharField("Статус заказа", choices=ST)
    price = models.DecimalField("Цена", decimal_places=2, max_digits=10)
    date = models.DateField("Дата заказа")
    delivery_address = models.TextField("Адрес доставки")
    payment_method = models.CharField("Способ оплаты", choices=PM)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return f"Заказ #{self.id} - {self.id_user}"
    
class Category(models.Model):
    name = models.CharField("Название категории")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]

    def __str__(self):
        return self.name
    
class Manufacturer(models.Model):
    name = models.CharField("Название производителя")
    country = models.CharField("Страна")

    class Meta:
        verbose_name = "Производитель"
        verbose_name_plural = "Производители"
        ordering = ["name"]

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField("Название товара")
    id_category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    id_manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, verbose_name="Производитель")
    description = models.TextField("Описание")
    price = models.DecimalField("Цена", decimal_places=2, max_digits=10)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ["name"]

    def __str__(self):
        return self.name
    
class Position(models.Model):
    id_order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name="Заказ")
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Товар")
    quantity = models.IntegerField("Количество")
    unit_price = models.DecimalField("Цена", decimal_places=2, max_digits=10)

    class Meta:
        verbose_name = "Позиция"
        verbose_name_plural = "Позиции"

    def __str__(self):
        return f"{self.id_product} x {self.quantity}"
    
class Review(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Товар")
    comment = models.CharField("Комментарий")
    date = models.DateField("Дата создания")

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self):
        return f"Отзыв от {self.id_user} на {self.id_product}"