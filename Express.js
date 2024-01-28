const express = require('express');
const bodyParser = require('body-parser');
const shlex = require('shlex');

const app = express();
const port = process.env.PORT || 3000;

const classes = {
  "Amenity": require('./models/amenity'),
  "BaseModel": require('./models/base_model'),
  "City": require('./models/city'),
  "Place": require('./models/place'),
  "Review": require('./models/review'),
  "State": require('./models/state'),
  "User": require('./models/user')
};

app.use(bodyParser.json());

app.post('/api/create', (req, res) => {
  const args = req.body;
  const className = args.class_name;
  if (!classes.hasOwnProperty(className)) {
    return res.status(400).json({ error: "Invalid class name" });
  }
  const newDict = args.attributes || {};
  const instance = new classes[className](newDict);
  instance.save().then(() => {
    res.status(201).json({ id: instance.id });
  }).catch(err => {
    console.error(err);
    res.status(500).json({ error: "Internal server error" });
  });
});

app.get('/api/show', (req, res) => {
  const className = req.query.class_name;
  const instanceId = req.query.instance_id;
  if (!classes.hasOwnProperty(className)) {
    return res.status(400).json({ error: "Invalid class name" });
  }
  const key = className + "." + instanceId;
  storage.all().then(allInstances => {
    const instance = allInstances[key];
    if (!instance) {
      return res.status(404).json({ error: "Instance not found" });
    }
    res.status(200).json({ instance: instance.to_dict() });
  }).catch(err => {
    console.error(err);
    res.status(500).json({ error: "Internal server error" });
  });
});

app.delete('/api/destroy', (req, res) => {
  const className = req.query.class_name;
  const instanceId = req.query.instance_id;
  if (!classes.hasOwnProperty(className)) {
    return res.status(400).json({ error: "Invalid class name" });
  }
  const key = className + "." + instanceId;
  storage.all().then(allInstances => {
    const instance = allInstances[key];
    if (!instance) {
      return res.status(404).json({ error: "Instance not found" });
    }
    storage.delete(instance).then(() => {
      res.status(200).json({ message: "Instance deleted successfully" });
    }).catch(err => {
      console.error(err);
      res.status(500).json({ error: "Internal server error" });
    });
  }).catch(err => {
    console.error(err);
    res.status(500).json({ error: "Internal server error" });
  });
});

app.put('/api/update', (req, res) => {
  const className = req.body.class_name;
  const instanceId = req.body.instance_id;
  const attribute = req.body.attribute;
  const value = req.body.value;

  if (!classes.hasOwnProperty(className)) {
    return res.status(400).json({ error: "Invalid class name" });
  }

  const key = className + "." + instanceId;
  storage.all().then(allInstances => {
    const instance = allInstances[key];
    if (!instance) {
      return res.status(404).json({ error: "Instance not found" });
    }
    instance[attribute] = value;
    instance.save().then(() => {
      res.status(200).json({ message: "Instance updated successfully" });
    }).catch(err => {
      console.error(err);
      res.status(500).json({ error: "Internal server error" });
    });
  }).catch(err => {
    console.error(err);
    res.status(500).json({ error: "Internal server error" });
  });
});

app.listen(port, () => {
  console.log(`QuickSearch Estate app listening at http://localhost:${port}`);
});

