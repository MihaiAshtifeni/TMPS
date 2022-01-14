from User import User
from UserBuilder import UserBuilder

user = UserBuilder.item().withFirstName("Mihai").withLastName("Astifeni").withAge(21).liveInStreet("Studentilor 21").build()
user.print()