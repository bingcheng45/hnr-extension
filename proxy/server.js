'use strict';

const express = require('express');
const cors = require('cors');
const helmet = require('helmet');
const logger = require('morgan');
const bodyParser = require('body-parser');
const createError = require('http-errors');
const attackRoute = require('./routes/attack');

const app = express();

app.use(logger('dev'));
app.use(cors());
app.use(helmet());
app.use(bodyParser({ extended: true }));
app.use(bodyParser.json());

app.use('/api/attack', attackRoute);

// catch 404 and forward to error handler
app.use((req, res, next) => {
    next(createError(404));
});

// error handler
app.use((err, req, res, next) => {
    // set locals, only providing error in development
    res.locals.message = err.message;
    res.locals.error = req.app.get('env') === 'development' ? err : {};

    // logging
    console.log(err);

    // return error to client
    res.status(err.status || 500);
    res.json({
        message: err.message
    });
});

app.listen(3000, () => {
    console.log('Server is running.');
});