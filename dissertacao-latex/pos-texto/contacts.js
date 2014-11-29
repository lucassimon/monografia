var express = require('express'),
router = express.Router(),
pg = require('pg'),
conString = "postgres://postgres:postgres@localhost/monografia-django";

router.get('/', function(req, res) {
    res.json({title:'Api de Pessoas e contatos'});
});


router.route('/v1/contatos/')
.get(function(req, res) {
  pg.connect(conString, function(err, client, done) {
     if(err) {
        res.status(400).send(err);
    }
    client.query(
        'select c.*, p.name from api_contact as c inner join api_person as p on c.person_id=p.id',
        function(err, result){
           done();

           if (err) {
              res.status(400).send(err);
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
});

module.exports = router;
