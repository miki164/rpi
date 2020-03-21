var express = require("express");
var router = express.Router();
const axios = require("axios");

router.get("/", function(req, res, next) {
    let a = url => {
        axios.get(url)
            //.then(response => console.log(response['data']))
            .then(response => {
                res.send(response['data'])
            });
    };
    a("https://www.n2yo.com/satellites/?c=1");
});

module.exports = router;