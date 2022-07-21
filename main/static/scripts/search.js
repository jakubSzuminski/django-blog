const search_field = document.getElementById("search"); //getting the "search" input field
const output = document.getElementById("posts-container"); //getting the container of the posts list

const pagination_number = 3; //how many posts on a page
let page_number = 1; //current page number
let pages = 1; //number of the last page

var posts = [] //array of posts 

//fill all posts + pagination
function populate(){
    output.innerHTML = ''; //clear the container (from the previous search)
    
    //if there are no posts - show "No found posts" and end this function
    if(posts.length == 0) {
        var no_posts_found = document.createElement("h2");
        no_posts_found.textContent = 'No posts found. Sorry :('
        no_posts_found.setAttribute('id', 'no-posts-found');
        output.appendChild(no_posts_found);
        return;
    }

    //adding posts
    for(let i = (page_number - 1) * pagination_number; i < Math.min(posts.length, (page_number * pagination_number)); i++) {
        output.appendChild(posts[i]);
    }

    //adding pagination
    pages = Math.ceil(posts.length/pagination_number);

    //creating pagination elements, buttons, and adding proper functions
    if(pages > 1) {
        var pagination_container = document.createElement("div");
        pagination_container.setAttribute('id', 'pagination-container');

        var pagination_break = document.createElement("span");
        pagination_break.textContent = '...';
        pagination_break.setAttribute('class', 'pagination-break');

        var pagination_prev = document.createElement("button");
        pagination_prev.textContent = '<';
        pagination_prev.setAttribute('id', 'pagination_prev');
        pagination_prev.addEventListener('click', () => {
            if(page_number > 1) page_number--;
            populate();
        });
        
        var pagination_next = document.createElement("button");
        pagination_next.textContent = '>';
        pagination_next.setAttribute('id', 'pagination-next');
        pagination_next.addEventListener('click', () => {
            if(page_number < pages) page_number++;
            populate();
        });

        var pagination_first = document.createElement("button");
        pagination_first.textContent = '1';
        pagination_first.setAttribute('id', 'pagination-first');
        pagination_first.addEventListener('click', () => {
            page_number = 1;
            populate();
        });
        
        var pagination_last = document.createElement("button");
        pagination_last.textContent = `${pages}`;
        pagination_last.setAttribute('id', 'pagination-last');
        pagination_last.addEventListener('click', () => {
            page_number = pages;
            populate();
        });

        var pagination_active = document.createElement('button');
        pagination_active.textContent = `${page_number}`;
        pagination_active.setAttribute('id', 'pagination-active');
        pagination_active.setAttribute('class', 'pagination-active');

        if(page_number > 1) pagination_container.appendChild(pagination_prev);
        
        if(page_number == 1) pagination_first.classList.add('pagination-active');
        pagination_container.appendChild(pagination_first); 
        
        if(page_number > 1 && page_number < pages) {
            if(page_number > 2) pagination_container.appendChild(pagination_break);
            pagination_container.appendChild(pagination_active);
            if(page_number < pages - 1) pagination_container.appendChild(pagination_break);
        } else if(pages  > 2){
            pagination_container.appendChild(pagination_break);
        }

        if(page_number == pages) pagination_last.classList.add('pagination-active');
        pagination_container.appendChild(pagination_last);

        if(page_number < pages) pagination_container.appendChild(pagination_next);

        output.appendChild(pagination_container);
    } 
}


//function that returns month 'name', example: 1 - 'Jan', 2 - 'Feb', ...
//this function is used when processing json data from the search
function toMonthName(monthNumber) {
    const date = new Date();
    date.setMonth(monthNumber - 1);
    return date.toLocaleString('en-US', {
        month: 'short',
    });
}

function getPosts(search_value=''){
    fetch("/search-posts", {
        body: JSON.stringify({ search_value: search_value }),
        method: "POST",
    })
    .then((res) => res.json())
    .then((data) => {
        if(data.length === 0) {
            posts = [];
            populate();
        } else {
            posts = []
    
            for(let i = 0; i < data.length; i++) {
                var post_tags_list = document.createElement('div');
                post_tags_list.classList.add('post-tags-list');

                for(let j = 0; j < data[i].tags.length; j++) {
                    var tag = document.createElement('span');
                    tag.classList.add('tag');
                    tag.textContent = `${data[i].tags[j]}`;
                    post_tags_list.appendChild(tag);
                }
    
                post_date = new Date(data[i].created_on);
                post_date_string = `${toMonthName(post_date.getMonth())} ${post_date.getDate()}, ${post_date.getYear() + 1900}` 
                
                var post_div = document.createElement('div');
                post_div.classList.add('post');
                
                var post_title = document.createElement('h1');
                var post_title_link = document.createElement('a');
                post_title_link.setAttribute('href', `posts/${data[i].slug}`);
                post_title_link.textContent = `${data[i].title}`;
                post_title.appendChild(post_title_link);

                var post_date_element = document.createElement('p');
                post_date_element.classList.add('post-date');
                post_date_element.textContent = `${post_date_string}`;

                var post_description = document.createElement('p');
                post_description.classList.add('post-description');
                post_description.textContent = `${data[i].description}`;

                var post_tags = document.createElement('div');
                post_tags.classList.add('post-tags');
                //can add the 'pricetag' svg here
                post_tags.appendChild(post_tags_list);


                post_div.appendChild(post_title);
                post_div.appendChild(post_date_element);
                post_div.appendChild(post_description);
                post_div.appendChild(post_tags);

                posts.push(post_div);
            }
    
            populate();
        }
    })
}

search_field.addEventListener('keyup', (e) => { //adding the event listener to the "search" input field
    const search_value = e.target.value; //getting the text that's inside the input field
    console.log(`Search value: '${search_value}'`)
    getPosts(search_value); //get all the posts connected with this value
});




