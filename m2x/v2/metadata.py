class Metadata(object):
  def __init__(self, api, **data):
      self.api = api

  def read_metadata(self):
    return self.api.get(self.metadata_path())

  def read_metadata_field(self, field):
    return self.api.get(self.metadata_field_path(field))

  def update_metadata(self, params):
    return self.api.put(self.metadata_path(), data=params)

  def update_metadata_field(self, field, value):
    return self.api.put(self.metadata_field_path(field), data={ "value": value })

  def metadata_field_path(self, field):
    return '%s/%s' % (self.metadata_path(), field)

  def metadata_path(self):
    return self.subpath('/metadata')
