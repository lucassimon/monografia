var express = require('express');
var router = express.Router();

router.get('/', function(req, res) {
	res.json({title:'Api de contatos'});
});

router.route('/v1/contatos')
	.get(function(req, res) {
		res.json({title:'Contatos - GET'});
	})
	.post(function(req, res) {
		res.json({title:'Contatos - POST'});
	});

router.route('/v1/contatos/:id')
	.get(function(req, res) {
		res.json({title:'Contato - GET by Id'});
	})
	.put(function(req, res) {
		res.json({title:'Contatos - PUT by Id'});
	})
	.delete(function(req, res) {
		res.json({title:'Contatos - DELETE by Id'});
	});

module.exports = router;
