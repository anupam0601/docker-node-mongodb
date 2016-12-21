var express = require('express');
var app = express();
var MongoClient = require('mongodb').MongoClient
  , assert = require('assert');

// Find all docs in mongo docker container
var findDocuments = function(db, callback) {
  // Get the documents collection 
  var collection = db.collection('my_coll');
  // Find some documents 
  collection.find({}).toArray(function(err, docs) {
    console.log("++++>",docs);
  });
}

// Connection URL 
var url = 'mongodb://mongo:27017/myproject';
// Use connect method to connect to the Server 
MongoClient.connect(url, function(err, db) {
  assert.equal(null, err);
  console.log("Connected correctly to server");
    findDocuments(db, function() {
       db.close();
    });
 });

app.get('/', function(req,res){
	res.send("Hello User");
});

app.listen('3000', function(){
	console.log("App listening on port 3000!");
});
