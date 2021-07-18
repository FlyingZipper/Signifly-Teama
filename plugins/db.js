import firebase from 'firebase/app'
import 'firebase/database'
import teamMembers from '~/team.json'

const TEAM_KEY = 'teams'

// returns a promise ?
const createTeam = (teamData) => {
  const TEAM_SLUG = (new Date()).getTime().toString(16)
  teamData.members = teamMembers.filter(m => teamData.members.includes(m.email))
  return firebase.database().ref(`${TEAM_KEY}/${TEAM_SLUG}`).set(teamData)
}

const _get = (ref) => {
  const dbRef = firebase.database().ref(ref)
  return dbRef.get()
}

const getTeams = () => {
  return _get(`${TEAM_KEY}/`)
}

const getTeam = (slug) => {
  return _get(`${TEAM_KEY}/${slug}`)
}

export default ({ app }, inject) => {
  inject('createTeam', createTeam)
  inject('getTeams', getTeams)
  inject('getTeam', getTeam)
}
