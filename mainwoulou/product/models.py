from django.db import models

from django.urls import reverse
from django.template.defaultfilters import slugify

# Create your models here.
from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.utils.translation import gettext as _
from .managers import CommentManager

# Create your models here.


class Category(models.Model):
    objects = CommentManager()
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name=_("Parent Category"),
    )

    class Meta:
        ordering = ("-created",)
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("categories:category-detail", kwargs={"pk": self.id})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def children(self):
        """Return replies of a Category."""
        return Category.objects.filter(parent=self)

    @property
    def is_parent(self):
        """Return `True` if instance is a parent."""
        if self.parent is not None:
            return False
        return True


class Product(models.Model):
    """
    Product Model class
    """
    
    class Meta:
        ordering = ("-created",)
        verbose_name = "Product"
        verbose_name_plural = "Products"

    category = models.ForeignKey(
        Category, related_name="products", on_delete=models.CASCADE
    )
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    name = models.CharField(max_length=200, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("products:product-detail", kwargs={"pk": self.slug})

