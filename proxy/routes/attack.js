'use strict';

const router = require('express').Router();
const request = require('request-promise-native');
const multer = require('multer');
const upload = multer({
    storage: multer.memoryStorage()
});

router.route('/')
    .post(upload.single('image'), async (req, res, next) => {
        try {
            const image = req.file;

            const formData = {
                image: image.buffer,
                potency: 'high'
            };

            const resp = await request.post({
                url: 'http://localhost:5000/api/attack',
                formData: formData
            });
            console.log(image.buffer);
            res.json({ message: image.buffer });
        } catch (err) {
            // console.log(err);
            return next(err);
        }
    });

module.exports = router;