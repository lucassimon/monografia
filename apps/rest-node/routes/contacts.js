var express = require('express');
var router = express.Router();
var pg = require('pg');
var conString = "postgres://postgres:postgres@localhost/monografia-django";

router.get('/', function(req, res) {
	res.json({title:'Api de Pessoas e contatos'});
});

router.route('/v1/pessoas/')
	.get(function(req, res) {
		pg.connect(conString, function(err, client, done) {
			if(err) {
				res.status(400);
				res.send(err);
			}
			client.query(
				'select * from api_person',
			   	function(err, result){
					done();

					if (err) {
						res.status(400);
						res.send(err);
					}

					res.json(
						{
							meta: {
								resource:'Pessoas',
								count:result.rows.length,
							},
							data:result.rows
						}
					);
				}
			);
		});
	})
	.post(function(req, res) {
		pg.connect(conString, function(err, client, done) {
			if(err) {
				res.status(400);
				res.send(err);
			}
			client.query(
				'INSERT INTO api_person(name, created, modified) VALUES($1, $2, $3)',
			   	[
					req.body.name,
				   	req.body.created,
				   	req.body.modified
				],
			   	function(err, result){
					done();

					if (err) {
						res.status(400);
						res.send(err);
					}

					res.status(201);
					res.json(
						{
							meta: {
								resource:'Pessoas',
							},
							message: 'Pessoa criado com sucesso'
						}
					);
				}
			);
		});
	});

router.route('/v1/pessoas/:id')
	.get(function(req, res) {
		pg.connect(conString, function(err, client, done) {
			if(err) {
				res.status(400);
				res.send(err);
			}
			client.query(
				'select * from api_person where id=$1::int',
				[
					req.params.id
				],
			   	function(err, result){
					done();

					if (err) {
						res.status(400);
						res.send(err);
					}

					res.json(
						{
							meta: {
								resource:'Pessoas',
								count:result.rows.length,
							},
							data:result.rows
						}
					);
				}
			);
		});
	})
	.put(function(req, res) {
		pg.connect(conString, function(err, client, done) {
			if(err) {
				res.status(400);
				res.send(err);
			}
			client.query(
				'UPDATE  api_person set name=$1,  modified=$2 where id=$3::int',
			   	[
					req.body.name,
				   	req.body.modified,
				   	req.params.id
				],
			   	function(err, result){
					done();

					if (err) {
						res.status(400);
						res.send(err);
					}

					res.status(201);
					res.json(
						{
							meta: {
								resource:'Pessoas',
							},
							message: 'Pessoa atualizada com sucesso'
						}
					);
				}
			);
		});
	})
	.delete(function(req, res) {
		pg.connect(conString, function(err, client, done) {
			if(err) {
				res.status(400);
				res.send(err);
			}
			client.query(
				'DELETE from api_person where id=$1::int',
			   	[
				   	req.params.id
				],
			   	function(err, result){
					done();

					if (err) {
						res.status(400);
						res.send(err);
					}

					res.json(
						{
							meta: {
								resource:'Pessoas',
							},
							message: 'Pessoa  deletada com sucesso'
						}
					);
				}
			);
		});
	});

router.route('/v1/contatos/')
	.get(function(req, res) {
		pg.connect(conString, function(err, client, done) {
			if(err) {
				res.status(400);
				res.send(err);
			}
			client.query(
				'select * from api_contact',
			   	function(err, result){
					done();

					if (err) {
						res.status(400);
						res.send(err);
					}

					res.json(
						{
							meta: {
								resource:'Contatos',
								count:result.rows.length,
							},
							data:result.rows
						}
					);
				}
			);
		});
	})
	.post(function(req, res) {
		res.json({title:'Contatos - POST'});
	});

router.route('/v1/contatos/:id')
	.get(function(req, res) {
		pg.connect(conString, function(err, client, done) {
			if(err) {
				res.status(400);
				res.send(err);
			}
			client.query(
				'select * from api_contact where id=$1::int',
				[
					req.params.id
				],
			   	function(err, result){
					done();

					if (err) {
						res.status(400);
						res.send(err);
					}

					var firstRow = result.rows[0], columns = [];
					for(var columnName in firstRow) {
						columns.push(columnName);
					}

					res.json(
						{
							meta: {
								resource:'Contatos',
								count:result.rows.length,
								columnCount: Object.keys(result.rows[0]).length,
								columns: columns
							},
							data:result.rows
						}
					);
				}
			);
		});
	})
	.put(function(req, res) {
		res.json({title:'Contatos - PUT by Id'});
	})
	.delete(function(req, res) {
		res.json({title:'Contatos - DELETE by Id'});
	});

module.exports = router;
