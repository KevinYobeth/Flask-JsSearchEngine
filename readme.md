# Javascript Snippet Search Engine - Documentation

## 1. Get Random Snippets

`GET` https://js-searchengine.herokuapp.com/

### Description

Returns 5 random javascript snippet. Returns the ID and Title of the code snippet.

### Parameters

`none`

### Response

`200 OK`

Body

```json
{
  "19": {
    "id": 19,
    "title": "allEqualBy"
  },
  "69": {
    "id": 69,
    "title": "converge"
  },
  "180": {
    "id": 180,
    "title": "httpDelete"
  },
  "280": {
    "id": 280,
    "title": "merge"
  },
  "435": {
    "id": 435,
    "title": "toSnakeCase"
  }
}
```

## 2. Search Snippet using TF-IDF

`POST` https://js-searchengine.herokuapp.com/search?query={query}

### Description

Search javascript snippets from database with given query. Returns the ID and Title of the snippets

### Parameters

`query: String of query to search.`

### Response

`200 OK`

Body

```json
{
  "117": {
    "id": 117,
    "title": "everyNth"
  },
  "191": {
    "id": 191,
    "title": "initial"
  },
  "310": {
    "id": 310,
    "title": "orderWith"
  },
  "327": {
    "id": 327,
    "title": "pluck"
  },
  "372": {
    "id": 372,
    "title": "sampleSize"
  },
  "381": {
    "id": 381,
    "title": "shuffle"
  },
  "410": {
    "id": 410,
    "title": "tail"
  },
  "449": {
    "id": 449,
    "title": "uniqueElements"
  },
  "90": {
    "id": 90,
    "title": "deepFlatten"
  }
}
```

## 3. Get code by ID

`GET` https://js-searchengine.herokuapp.com/code/{id}

### Description

Get the result of code ID. Returns the title, tags, description and the code itself.

### Parameters

`id: Code ID to find.`

### Response

`200 OK`

Body

```json
{
  "code": "const all = (arr, fn = Boolean) => arr.every(fn);\nall([4, 2, 3], x => x > 1); // true\nall([1, 2, 3]); // true",
  "description": "all: Checks if the provided predicate function returns true for all elements in a collection.\n\nUse Array.prototype.every() to test if all elements in the collection return true based on fn.\nOmit the second argument, fn, to use Boolean as a default.",
  "tags": "array,beginner",
  "title": "all"
}
```

### Response

`204 No Content`

Body

```json
{}
```
