//import Polls from 'modules/polls/Polls';
//import PollsDetail from 'modules/polls/PollsDetail';
//import PollsResults from 'modules/polls/PollsResults';
import SharedBooks from 'modules/core/SharedBooks/SharedBooks';
import AddBookToBookshelf from 'modules/core/AddBookToBookshelf/AddBookToBookshelf';
import GroupView from 'modules/core/GroupView/GroupView';
import LoadingPage from 'components/LoadingPage/LoadingPage'
import ConfirmPage from 'modules/core/ConfirmPage/ConfirmPage';
import LandingPage from 'components/Landing/Landing';
import ModulePage from 'components/ModulePage/ModulePage';
import NewsFeed from 'components/NewsFeed/NewsFeed';
import Story from 'components/Story/Story';
import Dashboard from 'components/Test/Dashboard';
import BuyComplete from 'components/BuyComplete/BuyComplete';


const coreRoutes = [
  {
    path: '/shared-books',
    component: SharedBooks,
  },
  {
    path: '/add-book',
    component: AddBookToBookshelf,
  },
  {
    path: '/group/:name_url',
    component: GroupView,
  },
  {
    path: '/becoming-friends',
    component: LoadingPage,
  },
  {
    path: '/setup',
    component: ConfirmPage,
  },
  {
    path: '/home',
    component: ModulePage,
  },
  {
    path: '/newsfeed',
    component: NewsFeed,
  },
  {
    path: "/Story",
    component: Story,
  },
  {
    path: "/Dashboard",
    component: Dashboard,
  },
  {
    path: "/Congrats",
    component: BuyComplete,
  }


  //{
    //path: '/polls/:id/detail',
    //component: PollsDetail,
  //},
  //{
    //path: '/polls/:id/results',
    //component: PollsResults,
  //},
  //{
    //path: '/polls/:id/vote',
    //component: PollsVote,
  //}

];

export default coreRoutes;
