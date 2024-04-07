document.addEventListener('DOMContentLoaded', function() {
    fetchBooks();
}, false);

function fetchBooks() {
    fetch('/api/books/')
        .then(response => response.json())
        .then(data => {
            const booksList = document.getElementById('books-list');
            booksList.innerHTML = '';
            data.forEach(book => {
                const bookItem = document.createElement('div');
                bookItem.textContent = `${book.title} (${book.publication_year}) - Author ID: ${book.author}, Genre IDs: ${book.genre.join(', ')}`;
                booksList.appendChild(bookItem);
            });
        })
        .catch(error => {
            console.error("Error fetching books: ", error);
            alert('Failed to fetch books.');
        });
}

function createBook() {
    const title = document.getElementById('title').value;
    const publicationYear = document.getElementById('publication_year').value;
    const author = document.getElementById('author').value;
    const genre = document.getElementById('genre').value.split(',').map(id => id.trim());

    fetch('/api/books/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            // 'Authorization': 'Bearer YOUR_ACCESS_TOKEN', // Commented out for public endpoints or implement dynamic token retrieval
        },
        body: JSON.stringify({
            title,
            publication_year: publicationYear,
            author,
            genre
        })
    }).then(response => {
        if (response.ok) {
            fetchBooks();
        } else {
            alert('Failed to create book.');
        }
    })
    .catch(error => {
        console.error("Error creating book: ", error);
        alert('Failed to create book due to an error.');
    });
}