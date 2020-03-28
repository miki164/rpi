var express = require("express");
var router = express.Router();
const axios = require("axios");
const cheerio = require("cheerio");

//Save your life, don't look at it.
router.get("/", function(req, res, next) {
    let a = url => {
        axios.get(url)
            .then(response => {
                const $ = cheerio.load(response['data']);
                let content = "<table>" +
                    "<tr><th>Name</th><th>noradid</th><th>Period[min]</th><th>Magnitude</th></tr>";

                $('table').eq(1)
                    .find('table')
                    .find('tr')
                    .each((i, elem) => {
                        const tds = $(elem).find('td');
                        const name = tds.eq(0).text();
                        const noradid = tds.eq(1).text();
                        const period = tds.eq(4).text();
                        const magnitude = tds.eq(5).text();
                        content += "<tr>"
                            + "<th><a href=\"satellite/"+noradid+"\">" + name+"</a></th>"
                            + "<th>" + noradid + "</th>" +
                            + "<th>" + period + "</th>"
                            + "<th>" + magnitude+ "</th>"
                            +"</tr>"
                    });

                content+="</table>";
                res.send(content);
            });
    };

    a("https://www.n2yo.com/satellites/?c=1");
});

module.exports = router;