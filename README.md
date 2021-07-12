# Gender extractor
Gender extractor is a tool that tries to guess the gender of a person given a name. 

I agree - there are already many projects like that, and most of them are written better (especially considering the fact that I've spent whooping 30 minutes on this one, most of which was focused on fighting the paths), but somehow I couldn't find anything on MIT license. However, if the licensing is not your concern, I invite you to use anything else (for example the greatly done https://github.com/tue-mdse/genderComputer).

So, here it is - a name-to-gender extractor on an MIT license.

## Usage
```python
from gender_extractor import GenderExtractor

ext = GenderExtractor()
print(ext.extract("Andrea"))
> 'female'
print(ext.extract("Andrea", "Italy"))
> 'male'

```

## Database
The database of the names was taken from the https://github.com/tue-mdse/genderComputer project, in which it was published under the [Open Database License](https://opendatacommons.org/licenses/odbl/1-0/).