from rest_framework import serializers

from apps.settings.models import Library,Book,Author,Booking,Reader,Borrowing

class LibrarySerilizer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = ['id', 'title', 'description', 'image']
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'description', 'price', 'author']

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'birth_year']

class BookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'description', 'price', 'author']

class BookRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'description', 'price', 'author']

class BookDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'description', 'price', 'author']

class BookUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'description', 'price', 'author']

class BookDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id']


class AuthorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'birth_year']

class AuthorRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'birth_year']

class AuthorUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'birth_year']

class AuthorDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'user', 'book', 'booked_at', 'return_date', 'is_active']

class BookingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'user', 'book', 'booked_at', 'return_date', 'is_active']
class RetrieveSerializer(serializers.ModelSerializer):
    reader = serializers.PrimaryKeyRelatedField(read_only=True)
    book = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Booking
        fields = ['id', 'user', 'book', 'booked_at', 'return_date', 'is_active']

    def create(self, validated_data):
        user = self.context['request'].user
        reader = Reader.objects.get(user=user)
        validated_data['reader'] = reader

        book = validated_data['book']
        if book.available_copies <= 0:
            raise serializers.ValidationError("Нет книг")

        borrowing = Borrowing.objects.create(**validated_data)
        return borrowing
    
class BorrowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrowing
        fields = ['id', 'reader', 'book', 'borrowed_at', 'returned', 'return_date']
