import React from 'react';
import cx from 'classnames';

import Analytics from '../analytics/GoogleAnalytics';
import Dispatcher from '../events/Dispatcher';
import './TalkPane.scss';
import AutoWidth from './AutoWidth';
import TermVis from './TermVis';
const TalkPane = React.createClass({
  propTypes: {
    selectedTalk: React.PropTypes.object,
    allTalks: React.PropTypes.array,
    onTalkSelect: React.PropTypes.func,
    touched: React.PropTypes.bool
  },

  componentWillMount() {
    window.addEventListener('resize', this._handleWindowResize);
  },

  componentWillUnmount() {
    window.removeEventListener('resize', this._handleWindowResize);
  },

  _handleWindowResize() {
    const debounceDelay = 200;

    // run initially
    if (this.resizeTimer == null) {
      this.forceUpdate();
    }

    clearTimeout(this.resizeTimer);
    this.resizeTimer = setTimeout(() => {
      this.forceUpdate();
      this.resizeTimer = null;
    }, debounceDelay);
  },

  _handleTalkSelect(talk) {
    const { onTalkSelect } = this.props;

    Analytics.trackEvent('quick-select-talk', talk.id);

    if (onTalkSelect) {
      onTalkSelect(talk);
    }
  },

  _handleTitleClick(evt) {
    const { selectedTalk } = this.props;
    Dispatcher.trigger(Dispatcher.events.navigateVideo, selectedTalk, 0);
    evt.preventDefault();
  },

  _renderQuickSelect() {
    const { allTalks, touched } = this.props;

    function renderTalk(talk, i) {
      return (
        <div> 
        </div>
      );
    }

    return (
      <div className={cx('talk-quick-select', { touched })}>
        <span className='help-text'></span>
        
      </div>
    );
  },

  _renderTalk() {
    const { selectedTalk, touched } = this.props;

    if (!selectedTalk) {
      return null;
    }

    return (
      <div>
        <header>
          
	  
        
               
         
        </header>
        <AutoWidth><TermVis data={selectedTalk} touched={touched} /></AutoWidth>
      </div>
    );
  },

  render() {
    const { selectedTalk } = this.props;

    return (
      <div className={cx('talk-pane', { 'has-talk': !!selectedTalk })}>
        {this._renderQuickSelect()}
        {this._renderTalk()}
      </div>
    );
  }
});

export default TalkPane;
