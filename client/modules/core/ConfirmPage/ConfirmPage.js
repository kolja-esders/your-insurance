import React from 'react'
import styles from './ConfirmPage.scss'
import Link from 'react-router-dom/es/Link'
import { Button, Divider, Form, Grid, Image, Popup } from 'semantic-ui-react'
import { graphql, createFragmentContainer } from 'react-relay';
import { logoutViewer } from 'modules/auth/jwtUtils'
import { authenticatedRoute } from 'modules/auth/utils'
import ProfileImage from 'components/ProfileImage/ProfileImage.js'
import img from '../../../assets/logo2.png'


let getActivity = function(name, frequency) {
  return (
    <div className={styles.entityContainer}>
      <span className={styles.entity}>{ name }</span>
      <span className={styles.freq}>{ frequency }</span>
    </div>
  );
}

class ConfirmPage extends React.Component {

  render() {
    console.log(this.props.viewer)
    const user = this.props.viewer.user;
    
    return (
      <header className={styles.root}>
        <div className={styles.personal}>
          <ProfileImage imagePath="https://scontent-ams3-1.xx.fbcdn.net/v/t31.0-8/15271783_1242828795739861_3065007741581304786_o.jpg?oh=bc827532805d7e451af6ffa279e01a32&oe=5A7B1765" />
          <h1 className={styles.name}>{ user.firstName }<span className={styles.welcome}>, verify your data.</span></h1>
        </div>
        <Form>
          <section className={styles.infoSection}>
          {/*<header>
              <h2>About You</h2>
            </header> */}

            <Grid divided='vertically'>
              <Grid.Row columns={2}>
                <Grid.Column>
                  <div className={styles.greetingEmoji}></div>

                  <Form.Field>
                    <label>First name</label>
                    <input placeholder='First name' value={ user.firstName }/>
                  </Form.Field>
                  <Form.Field>
                    <label>Last name</label>
                    <input placeholder='Last name' value={ user.lastName }/>
                  </Form.Field>
                  <Form.Field>
                    <label>Age</label>
                    <input placeholder='Age' value='24'/>
                  </Form.Field>
                  <Form.Field>
                    <label>Employer / School</label>
                    <input placeholder='Employer / School' value='Karlsruhe Institute of Technology'/>
                  </Form.Field>
                </Grid.Column>

                <Grid.Column>
                  <div className={styles.homeEmoji}></div>

                  <Form.Field>
                    <label>Street address</label>
                    <input placeholder='' value='Hildebrandstr. 39'/>
                  </Form.Field>
                  <Form.Field>
                    <label>City</label>
                    <input placeholder='City' value='Karlsruhe'/>
                  </Form.Field>
                  <Form.Field>
                    <label>Zip code</label>
                    <input placeholder='Zip code' value='76227'/>
                  </Form.Field>
                </Grid.Column>
              </Grid.Row>
            </Grid>
          </section>

          <section className={styles.infoSection}>
            <Grid divided='vertically'>
              <Grid.Row columns={2}>
                <Grid.Column>
                  <div className={styles.runningEmoji}></div>
                    <Popup position='left center' inverted hoverable trigger= { getActivity('Snowboarding', 'Enthusiastic, 2x in the past month') }>Facebook post from the 12th Sept. 2017.
                    </Popup>
                    <Popup position='left center' inverted hoverable trigger= { getActivity('Running', 'Casual, 1x in the past month') }>Facebook post from the 12th Sept. 2017.
                    </Popup>
                </Grid.Column>

                <Grid.Column>
                  <div className={styles.sunEmoji}></div>
                  <Popup position='right center' inverted hoverable trigger= { getActivity('Smoking', 'Daily') }>
                    Facebook post from the 12th Sept. 2017.
                  </Popup>
                  <Popup position='right center' inverted hoverable trigger= { getActivity('Concerts', 'Yearly') }>
                    Facebook post from the 12th Sept. 2017.
                  </Popup>
                </Grid.Column>
              </Grid.Row>
            </Grid>
          </section>

          <section className={styles.infoSection}>
            <Grid divided='vertically'>
              <Grid.Row columns={2}>
                <Grid.Column>
                  <div className={styles.deviceEmoji}></div>
                    <Popup position='left center' inverted hoverable trigger= { getActivity('Smartphone', '~ 1,000 €') }>Facebook post from the 12th Sept. 2017.
                    </Popup>
                    <Popup position='left center' inverted hoverable trigger= { getActivity('Oven', '~ 3.200 €') }>Facebook post from the 12th Sept. 2017.
                    </Popup>
                </Grid.Column>

                <Grid.Column>
                  <div className={styles.familyEmoji}></div>
                  <Popup position='right center' inverted hoverable trigger= { getActivity('Cassandra', '32 years old') }>
                    Facebook profile information.
                  </Popup>
                  <Popup position='right center' inverted hoverable trigger= { getActivity('Anna', '12 years old') }>
                    Facebook profile information.
                  </Popup>
                  <Popup position='right center' inverted hoverable trigger= { getActivity('Tom', '10 years old') }>
                    Facebook profile information.
                  </Popup>
                </Grid.Column>
              </Grid.Row>
            </Grid>
          </section>

          <section className={styles.infoSection}>
            <Grid divided='vertically'>
              <Grid.Row columns={2}>
                <Grid.Column>
                  <div className={styles.injuryEmoji}></div>
                    <Popup position='left center' inverted hoverable trigger= { getActivity('Snowboarding', 'Enthusiastic') }>Facebook post from the 12th Sept. 2017.
                    </Popup>
                    <Popup position='left center' inverted hoverable trigger= { getActivity('Running', 'Casual') }>Facebook post from the 12th Sept. 2017.
                    </Popup>
                </Grid.Column>

                <Grid.Column>
                  <div className={styles.vacationEmoji}></div>
                  <Popup position='right center' inverted hoverable trigger= { getActivity('Bali', 'In April') }>
                    Facebook post from the 12th Sept. 2017.
                  </Popup>
                  <Popup position='right center' inverted hoverable trigger= { getActivity('Mallorca', 'In January') }>
                    Facebook post from the 12th Sept. 2017.
                  </Popup>
                </Grid.Column>
              </Grid.Row>
            </Grid>
          </section>

        </Form>

        <h1 className={styles.brand_name}>
          <Button as={Link} color="green" size="huge" fluid to="/home" className={styles.continueBtn}>Get quote</Button>
        </h1>
      </header>
    )
  }
}

const AuthenticatedConfirmPage = authenticatedRoute(ConfirmPage);

export default createFragmentContainer(
  AuthenticatedConfirmPage,
  graphql`
    fragment ConfirmPage_viewer on Viewer {
      id
      user {
        email
        firstName
        lastName
      }
    }
  `,
)
