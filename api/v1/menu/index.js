const express = require('express');
const router = express.Router();
const moment = require('moment');
const OverviewMenu = require('../../../db').OverviewMenu;
const DetailedMenu = require('../../../db').DetailedMenu;
const ActLevel = require('../../../db').ActLevel;
const Hours = require('../../../db').Hours;

// Get overview menu from today til the next 7 days
router.get('/OverviewMenu', (req, res) => {
    let startDate = moment().startOf('day').toDate();
    let endDate = moment().startOf('day').add(7, 'days').toDate();
    OverviewMenu.findAllByDateRange(startDate,endDate).then(menus => {
        res.json({ menus });
    });
});

router.get('/DetailedMenu', (req, res) => {
    let startDate = moment().startOf('day').toDate();
    let endDate = moment().startOf('day').add(7, 'days').toDate();
    OverviewMenu.findAllByDateRange(startDate,endDate).then(menus => {
        res.json({ menus });
    });
});

router.get('/ActivityLevels', (req, res) => {
    ActLevel.findLast().then(level => {
        res.json({ level });
    });
});

// router.get('/Hours', (req, res) => {
//     ActLevel.findLast().then(hours => {
//         res.json({ hours });
//     });
// });

// Test functions, for functionality
router.get('/test', (req, res) => {
    json_obj = {
        "test1": "Hello World",
        "test2": "Hi",
    };
    // OverviewMenu.create({overviewMenu: json_obj}).then(new_menu => {
    //     console.log(new_menu.getOverviewMenu());
    // });
    // Menu.findByID(4).then((menu) => {
    //     console.log(menu.getMenu());
    // });
    // Menu.Delete(16).then(deleted_menu => {
    //     console.log(deleted_menu);
   // });
    // let predate = moment().subtract(1,'hours');
    // OverviewMenu.findByDateRange(predate.toDate(), moment().toDate()).then(menus => {
    //     console.log(menus);
    // });
    OverviewMenu.findAllByDate(moment().startOf('day').toDate()).then(menus => {
        console.log(menus.length);
    });
});

module.exports = { router };