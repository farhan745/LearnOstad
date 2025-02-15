// Modal functions
function openModal(postId) {
  const modal = document.getElementById("postModal");
  if (modal) {
    document.body.classList.add("modal-open");
    modal.classList.remove("hidden");
    modal.classList.add("flex");
  }
  fetch(`https://basic-blog.teamrabbil.com/api/post-details/${postId}`)
    .then((response) => response.json())
    .then((data) => {
      document.querySelector("#postContent").textContent =
        data["postDetails"]["content"];
      document.querySelector("#img1").src = data["postDetails"]["img"];
      const commentList = document.querySelector("#commentList");
      data.postComments.forEach((el) => {
        commentList.innerHTML += `
            <div class="bg-white p-6 rounded-xl shadow-sm border border-gray-100">
                            <div class="flex items-center gap-3 mb-3">
                                <div
                                    class="w-10 h-10 rounded-full bg-purple-100 flex items-center justify-center text-purple-600 font-semibold">
                                    ${el.author[0].toUpperCase()}
                                </div>
                                <div>
                                    <div class="font-semibold text-gray-800">${
                                      el.author
                                    }</div>
                                    <div class="text-sm text-gray-500">December 15, 2024</div>
                                </div>
                            </div>
                            <p class="text-gray-600 leading-relaxed">${
                              el.comment
                            }</p>
                        </div>`;
      });
    });
}

function closeModal() {
  const modal = document.getElementById("postModal");
  if (modal) {
    modal.classList.remove("flex");
    modal.classList.add("hidden");
    document.body.classList.remove("modal-open");
  }
}

// Close modal when clicking outside
document.getElementById("postModal")?.addEventListener("click", function (e) {
  if (e.target === this) {
    closeModal();
  }
});

function categorySelect(id) {
  fetch(`https://basic-blog.teamrabbil.com/api/post-list/${id}`)
    .then((response) => response.json())
    .then((data) => {
      postList.innerHTML = "";
      data.forEach((el) => {
        postList.innerHTML += `<article
                            class="bg-white rounded-2xl shadow-sm hover:shadow-xl transition-all overflow-hidden group">
                            <div class="relative overflow-hidden">
                                <img src="${el.img}" alt="Post Title"
                                    class="w-full h-56 object-cover transform group-hover:scale-105 transition-transform duration-300">
                                <div class="absolute top-4 left-4">
                                    <span
                                        class="px-4 py-2 bg-white/90 backdrop-blur-sm rounded-lg text-purple-600 text-sm font-semibold">
                                        Technology
                                    </span>
                                </div>
                            </div>
                            <div class="p-6">
                                <h3
                                    class="text-xl font-bold text-gray-800 mb-3 group-hover:text-purple-600 transition-colors">
                                    ${el.title}
                                </h3>
                                <p class="text-gray-600 mb-4 line-clamp-2">
                                    ${el.short}
                                </p>
                                <div class="flex items-center justify-between">
                                    <span class="text-sm text-gray-500">Dec 15, 2024</span>
                                    <button onclick="openModal(${el.id})"
                                        class="text-purple-600 hover:text-purple-700 font-medium inline-flex items-center gap-2 transition-colors">
                                        Read more →
                                    </button>
                                </div>
                            </div>
                        </article>`;
      });
    });
}

const catButtons = document.querySelector("#categoryButtons");
//const categories=["Technology","Plant","Sports","Art","Health"];
axios("https://basic-blog.teamrabbil.com/api/post-categories").then((data) => {
  data.data.forEach((el) => {
    catButtons.innerHTML += `<button 
        onclick="categorySelect(${el.id})" 
        class="px-4 py-2 rounded-xl bg-gray-100 text-gray-600 hover:bg-purple-600 hover:text-white hover:shadow-lg hover:shadow-purple-200 transition-all text-sm sm:text-base whitespace-nowrap">
        ${el["name"]}
    </button>`;
  });
});

const categoriesBottom = document.querySelector("#catBot");
axios("https://basic-blog.teamrabbil.com/api/post-categories").then((data) => {
  data.data.forEach((el) => {
    categoriesBottom.innerHTML += `<li><a href="#" onclick="categorySelect(${el.id})"  class="text-gray-400 hover:text-purple-400 transition-colors">${el.name}</a>`;
  });
});
const postList = document.querySelector("#postList");
fetch("https://basic-blog.teamrabbil.com/api/post-newest")
  .then((response) => response.json())
  .then((data) => {
    postList.innerHTML = "";
    data.forEach((el) => {
      postList.innerHTML += `<article
                        class="bg-white rounded-2xl shadow-sm hover:shadow-xl transition-all overflow-hidden group">
                        <div class="relative overflow-hidden">
                            <img src="${el.img}" alt="Post Title"
                                class="w-full h-56 object-cover transform group-hover:scale-105 transition-transform duration-300">
                            <div class="absolute top-4 left-4">
                                <span
                                    class="px-4 py-2 bg-white/90 backdrop-blur-sm rounded-lg text-purple-600 text-sm font-semibold">
                                    Technology
                                </span>
                            </div>
                        </div>
                        <div class="p-6">
                            <h3
                                class="text-xl font-bold text-gray-800 mb-3 group-hover:text-purple-600 transition-colors">
                                ${el.title}
                            </h3>
                            <p class="text-gray-600 mb-4 line-clamp-2">
                                ${el.short}
                            </p>
                            <div class="flex items-center justify-between">
                                <span class="text-sm text-gray-500">Dec 15, 2024</span>
                                <button onclick="openModal(${el.id})"
                                    class="text-purple-600 hover:text-purple-700 font-medium inline-flex items-center gap-2 transition-colors">
                                    Read more →
                                </button>
                            </div>
                        </div>
                    </article>`;
    });
  });

function setupCommentForm(postId) {
    const commentForm = document.getElementById('commentForm');

    // Remove existing event listeners (if any) to prevent duplicate handlers
    commentForm.replaceWith(commentForm.cloneNode(true));
    const newCommentForm = document.getElementById('commentForm');

    newCommentForm.addEventListener('submit', function (event) {
        event.preventDefault(); // Prevent the default form submission

        // Create a new FormData object from the form
        const formData = new FormData(newCommentForm);

        // Add the custom key-value pair (list_id)
        const customData = new FormData();
        customData.append('list_id', postId);

        // Add all the form data to the customData object
        formData.forEach((value, key) => {
            customData.append(key, value);
        });

        // Convert FormData to a plain object
        const formObject = {};
        customData.forEach((value, key) => {
            formObject[key] = value;
        });

        // Send the data via a POST request
        fetch('https://basic-blog.teamrabbil.com/api/create-comment', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formObject),
        })
            .then((response) => response.json())
            .then((data) => {
                console.log('Success:', data);
                newCommentForm.reset(); // Reset the form

                // Reload comments
                fetch(`https://basic-blog.teamrabbil.com/api/post-details/${postId}`)
                    .then((response) => response.json())
                    .then((updatedData) => {
                        loadComments(updatedData); // Refresh the comments list
                    })
                    .catch((error) => console.error('Error reloading comments:', error));
            })
            .catch((error) => console.error('Error submitting comment:', error));
    });
}

