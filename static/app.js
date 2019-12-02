const searchClient = algoliasearch(
  'BQFJ9HIZXY',
  '16dd2937e571aea119a0ca79ba7117d4'
);

const search = instantsearch({
  indexName: 'book_search',
  searchClient,
});

search.addWidget(
  instantsearch.widgets.searchBox({
    container: '#searchbox',
    placeholder: "Search for books",
    magnifier: false
  })
);

search.addWidget(
  instantsearch.widgets.hits({
    container: '#hits',
    hitsPerPages: 10,
    templates: {
      item: `
      <article >
      <div id = "hit">
        <div class = "hit-image_url">
          <img src="{{image_url}}" alt="{{name"}}">
          </div>
          <div class = "hit-title">
          <h4><a>{{#helpers.highlight}}{ "attribute": "title" }{{/helpers.highlight}}</a></h4>
          </div>
          </div>

        </article>
      `,
    },
  })
);

search.addWidget(
  instantsearch.widgets.pagination({
    container: '#pagination',
  })
);

search.start();
