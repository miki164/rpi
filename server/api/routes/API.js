var express = require("express");
var router = express.Router();
const axios = require("axios");
const cheerio = require("cheerio");

router.get("/", function(req, res, next) {
    let a = url => {
        if(req.params) {
            axios.get(url)
                .then(response => {
                    const $ = cheerio.load(response['data']);
                    let content = "";
                    let j = 0;
                    $('table').eq(1).find('table')
                        .find('a').each((i, elem) => {
                            let href = $(elem).attr('href').replace("/?s=", "/");
                            console.log(href);
                            if(href.startsWith("/s")) {
                                j+=1;
                                content += i+1 + ".<a href=\""+href+"\">"+$(elem).text()+"</a></br>"
                            }
                        }).html();
                    res.send(content);
                });
        }
    };
    a("https://www.n2yo.com/satellites/?c=1");
});

module.exports = router;